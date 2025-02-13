from .db_connection import db_connection
from dotenv import load_dotenv
from openai import OpenAI
from .generate_tools_schema import generate_json_schema
import json
from copy import deepcopy
import streamlit as st  # 导入 Streamlit

load_dotenv()

class tiny_sql_agent:
    def __init__(self, db, sensitive_database=False):
        self.db = db
        # 从 Streamlit Secrets 中读取 OpenAI API Key
        self.client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # 使用 st.secrets 读取 API Key
        self.sensitive_database = sensitive_database
        self.tools = [
            generate_json_schema(i)
            for i in [
                self.db.get_tables,
                self.db.get_schema,
                self.db.get_create_statement,
                self.db.run_query,
            ]
        ]
        self.generated_sql = None  # Variable to store generated SQL query

    def privacy_check(self, query):
        """Basic privacy filter for sensitive databases."""
        sensitive_terms = ["medical record", "patient_id", "confidential"] if self.sensitive_database else []
        identification_patterns = ["unique subject", "specific patient", "individual identifier"] if self.sensitive_database else []
        
        if any(term.lower() in query.lower() for term in sensitive_terms + identification_patterns):
            return "Denied: This query attempts to identify specific subject data, which is restricted for privacy."

        modification_terms = ["delete", "update", "insert", "drop", "alter"]
        first_word = query.strip().split()[0].lower()

        if first_word in modification_terms:
            return "Denied: Only read-only queries and 'CREATE VIEW' statements are permitted."

        return None

    def run(self, query, return_sql=False):
        """
        Interprets the query, forms SQL, executes it, and returns results.
        If return_sql=True, always return a 2-tuple (sql_query_or_None, result_or_message).
        """
        privacy_violation = self.privacy_check(query)
        if privacy_violation:
            # Return a tuple indicating no SQL was generated
            return (None, privacy_violation)

        # Capture SQL query generated within self.db.run_query
        self.generated_sql = None

        # Store the original run_query method
        original_run_query = self.db.run_query

        # Define a wrapper to capture the SQL
        def capture_sql_wrapper(*args, **kwargs):
            self.generated_sql = kwargs.get('query') or args[0]
            print(f"Captured SQL: {self.generated_sql}")  # Debugging statement
            return original_run_query(*args, **kwargs)

        # Temporarily replace self.db.run_query with the wrapper
        self.db.run_query = capture_sql_wrapper

        try:
            assistant = self.client.beta.assistants.create(
                model='gpt-4o-2024-08-06',
                instructions="""
                    You are a SQL query agent designed to assist users with database queries. Your primary function is to interpret natural language questions about the database and convert them into accurate SQL queries. Your key responsibilities include:

                    1. Analyzing the user's question carefully to understand the data they’re seeking.
                    2. Formulating a SQL query to retrieve the requested information from the database.
                    3. Ensuring that the query does not reveal private or sensitive information, particularly for medical data.
                    4. Limiting the query to read-only access or allowing 'CREATE VIEW' statements without other modifications to the database.
                    5. Executing the SQL query using the provided database connection.
                    6. Interpreting the query results and providing a clear, concise answer to the user’s original question, without exposing identifiable information.
                """,
                tools=self.tools,
                name="sql-query-agent",
            )

            thread = self.client.beta.threads.create()
            self.client.beta.threads.messages.create(thread_id=thread.id, role="user", content=query)
            run = self.client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant.id)

            max_turns = 50
            for _ in range(max_turns):
                if run.status == "completed":
                    # Retrieve the final message to get the result
                    messages = self.client.beta.threads.messages.list(
                        thread_id=thread.id, run_id=run.id, order="asc"
                    )
                    # Extract result from the last message
                    last_message_content = messages.data[-1].content if messages.data else None
                    result = next(
                        (content.text.value for content in last_message_content if content.type == "text"),
                        None
                    )

                    if return_sql:
                        # Return tuple
                        return (self.generated_sql, result)
                    else:
                        # Return just the result
                        return result

                elif run.status == "requires_action":
                    func_tool_outputs = []
                    for tool in run.required_action.submit_tool_outputs.tool_calls:
                        if hasattr(self.db, tool.function.name) and callable(getattr(self.db, tool.function.name)):
                            func_output = getattr(self.db, tool.function.name)(**json.loads(tool.function.arguments))
                            func_tool_outputs.append({"tool_call_id": tool.id, "output": str(func_output)})
                        else:
                            raise Exception(f"Function not available: {tool.function.name}")

                    run = self.client.beta.threads.runs.submit_tool_outputs_and_poll(
                        thread_id=thread.id,
                        run_id=run.id,
                        tool_outputs=func_tool_outputs
                    )

                elif run.status == "failed":
                    print(f"Agent run failed for the reason: {run.last_error}")
                    # Return tuple with error
                    return (None, f"Agent run failed for the reason: {run.last_error}")

                else:
                    print(f"Run status {run.status} not yet handled")
            else:
                print("Reached maximum reasoning turns, maybe increase the limit?")
                return (None, "Reached maximum reasoning turns")

        finally:
            # Restore the original run_query method
            self.db.run_query = original_run_query

    def filter_sensitive_information(self, result):
        # Implement any filtering logic to remove sensitive information from the result
        return result