import streamlit as st
from tiny_sql_agent.db_connection import db_connection
from tiny_sql_agent.tiny_sql_agent import tiny_sql_agent
import tempfile
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Streamlit setup
st.set_page_config(layout="wide", page_title="SQL Genius", page_icon="🚀")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General styles */
    .block-container {
        padding: 2rem 4rem;
        max-width: 1200px;
        margin: auto;
    }
    .title {
        margin-top: 20px;
        margin-bottom: 40px;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #2E86C1;  /* Modern blue color */
        font-family: 'SF Pro Display', 'Arial', sans-serif;
    }
    .section-header {
        font-size: 28px;
        font-weight: bold;
        font-family: 'SF Pro Display', 'Arial', sans-serif;
        color: #34495E;  /* Dark gray for headers */
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #EAEDED;  /* Subtle border */
    }
    .description {
        font-size: 18px;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        color: #566573;  /* Soft gray for text */
        margin-bottom: 20px;
        line-height: 1.6;
    }
    .success-message {
        color: #27AE60;  /* Green for success */
        background-color: #E8F8F5;  /* Light green background */
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    }
    .error-message {
        color: #E74C3C;  /* Red for errors */
        background-color: #FDEDEC;  /* Light red background */
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    }
    .stTextArea>div>textarea {
        font-size: 18px !important;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        border-radius: 8px;
        border: 1px solid #D5D8DC;  /* Light border */
        padding: 12px;
    }
    .stCodeBlock {
        font-size: 16px;
        font-family: 'SF Mono', 'Courier New', monospace;
        background-color: #F4F6F6;  /* Light gray background */
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #D5D8DC;  /* Light border */
    }
    .stDownloadButton button {
        font-size: 16px;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        background-color: #2E86C1;  /* Modern blue */
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    }
    .stButton>button {
        font-size: 18px;
        font-family: 'SF Pro Text', 'Arial', sans-serif;
        background-color: #2E86C1;  /* Modern blue */
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        transition: background-color 0.3s ease;  /* Smooth hover effect */
    }
    .stButton>button:hover {
        background-color: #2471A3;  /* Darker blue on hover */
    }
    .ag-theme-streamlit {
        --ag-header-background-color: #F4F6F6;  /* Light gray for header */
        --ag-header-foreground-color: #34495E;  /* Dark gray for text */
        --ag-border-color: #D5D8DC;  /* Light border */
        --ag-row-hover-color: #EAEDED;  /* Light gray on hover */
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    }
    </style>
    """, unsafe_allow_html=True
)

# Title with consistent style and color
st.markdown('<div class="title">SQL Genius 🚀</div>', unsafe_allow_html=True)

# Introduction and Usage Guide
st.markdown('<div class="section-header">How to Use This Interface</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="description">
        Welcome to the SQL Genius Interface! Here's how you can use it:
        <ol>
            <li>Select a database from the options below.</li>
            <li>Enter a natural language question in the query box.</li>
            <li>Click "Execute Query" to generate and run the SQL query.</li>
            <li>View the generated SQL and query results below.</li>
        </ol>
        Here are some example questions you can try based on the selected database:
    </div>
    """, unsafe_allow_html=True
)

# Database Selection
st.markdown('<div class="section-header">Choose a Database <img src="https://img.icons8.com/ios-filled/50/000000/database.png" alt="Database Icon" style="vertical-align: middle; width: 20px; height: 20px;"></div>', unsafe_allow_html=True)
db_choice = st.radio(
    "",  # Empty label for cleaner appearance
    ("Chinook.db", "Northwind.db", "VitalDB.db", "Upload your own .db file"),
    index=0,
    key="db_choice"
)

# Example Questions for Each Database
if db_choice == "Chinook.db":
    st.markdown(
        """
        <div class="description">
            Example Questions for <b>Chinook.db</b>:
            <ul>
                <li>What is the total price for the album “Big Ones”?</li>
                <li>Which country's customers spent the most? And how much did they spend?</li>
                <li>What was the most purchased track of 2013?</li>
                <li>How many albums does the artist Led Zeppelin have?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
elif db_choice == "Northwind.db":
    st.markdown(
        """
        <div class="description">
            Example Questions for <b>Northwind.db</b>:
            <ul>
                <li>Find the name of the customer who placed the most orders.</li>
                <li>What were our total revenues in 1997?</li>
                <li>What is the total amount of customer ALFKI has paid us so far?</li>
                <li>Identify the top 3 products with the highest total quantity sold.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
elif db_choice == "VitalDB.db":
    st.markdown(
        """
        <div class="description">
            Example Questions for <b>VitalDB.db</b>:
            <ul>
                <li>How much PPF was administered in the top 3 cases by total administration?</li>
                <li>What are the details of the first three cases in clinical_data?</li>
                <li>What are the top 3 highest lab test results for 'alb' across all cases?</li>
                <li>What are the anesthesia start times for the first 3 cases based on earliest start times?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# File Uploader for Custom Database
uploaded_file = None
if db_choice == "Upload your own .db file":
    uploaded_file = st.file_uploader("Upload your .db file", type="db")

if "db_path" not in st.session_state:
    st.session_state.db_path = ""

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        st.session_state.db_path = tmp_file.name
else:
    st.session_state.db_path = f"./{db_choice}"

# Query Input and Results
st.markdown('<div class="section-header">Enter Your Query ✍️</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Ask a natural language question, and I\'ll generate the SQL query for you:</div>', unsafe_allow_html=True)
query = st.text_area("", height=150, placeholder="Type your question here...")

# Initialize session state for API call count
if "api_call_count" not in st.session_state:
    st.session_state.api_call_count = 0

# Maximum allowed API calls per day
MAX_API_CALLS = 100  # 设置每天最多 100 次 API 调用

# 预设的异常消息回复
INVALID_QUERY_RESPONSE = "Sorry, I couldn't understand your question. Please ask a clear and relevant question about the database."

# 超过 API 调用限制时的可爱提示信息
API_LIMIT_MESSAGE = """
<div class="description" style="text-align: center; color: #2E86C1; font-size: 20px;">
    <p>🌟 Oh no! It looks like you've used up your free daily quota of 100 queries. 🌟</p>
    <p>Don't worry, though! You can come back tomorrow for more SQL magic. 🪄✨</p>
    <p>Thank you for using SQL Genius! 💖</p>
</div>
"""

if "generated_sql" not in st.session_state:
    st.session_state.generated_sql = ""
if "result" not in st.session_state:
    st.session_state.result = ""

if st.button("Execute Query"):
    if query:
        if st.session_state.api_call_count >= MAX_API_CALLS:
            # 超过调用限制时显示可爱提示信息
            st.markdown(API_LIMIT_MESSAGE, unsafe_allow_html=True)
        else:
            try:
                # Initialize database connection and SQL agent
                database = db_connection(st.session_state.db_path)
                sql_agent = tiny_sql_agent(database, sensitive_database=True)

                # Fetch the generated SQL and result
                generated_sql, result = sql_agent.run(query, return_sql=True)
                st.session_state.generated_sql = generated_sql
                st.session_state.result = result

                # Increment API call count
                st.session_state.api_call_count += 1

                # Success message
                st.markdown('<div class="success-message">Query executed successfully! 🎉</div>', unsafe_allow_html=True)
            except Exception as e:
                # 异常消息处理：如果用户输入无关或混乱的消息，返回预设内容
                st.markdown(f'<div class="error-message">{INVALID_QUERY_RESPONSE}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="error-message">Please enter a valid query.</div>', unsafe_allow_html=True)

# Display Generated SQL
if st.session_state.generated_sql:
    st.markdown('<div class="section-header">Generated SQL Query:</div>', unsafe_allow_html=True)
    st.code(st.session_state.generated_sql, language='sql')

# Display Query Results with adjustable table height
st.markdown('<div class="section-header">Query Results:</div>', unsafe_allow_html=True)
if st.session_state.result:
    try:
        # Parse the result into a DataFrame
        rows = st.session_state.result.strip().split("\n")
        headers = rows[0].split(";")
        data = [row.split(";") for row in rows[1:] if row]
        df = pd.DataFrame(data, columns=headers)

        # Set dynamic table height based on number of rows
        table_height = min(400, 40 + 40 * len(df))  # Dynamic height with a max limit of 400px

        # Display using AgGrid
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(resizable=True, wrapText=True)
        grid_options = gb.build()
        AgGrid(df, gridOptions=grid_options, height=table_height, fit_columns_on_grid_load=True, theme="streamlit")

        # Add a download button for CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results as CSV", csv, "results.csv", "text/csv")
    except Exception as e:
        st.markdown(f'<div class="error-message">Error displaying results: {e}</div>', unsafe_allow_html=True)
        st.text(st.session_state.result)
else:
    st.info("Query results will appear here.")