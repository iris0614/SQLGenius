import sqlite3

class db_connection:
    def __init__(self, db_path):
        # self.connection = sqlite3.connect(db_path)
        # Force UTF-8 Encoding on the Connection: When you open the SQLite connection, set detect_types and text_factory to ensure the connection handles encoding issues.
        self.connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.connection.text_factory = lambda x: x.decode("utf-8", "ignore")  # Ignore decoding errors
        self.cursor = self.connection.cursor()

    def get_tables(self):
        # Get all tables using sqlite3
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        print(tables)
        return tables

    def get_schema(self, table_name):
        # Fetch and print schema for each table
        print(f"Schema for table '{table_name}':")
        # self.cursor.execute(f"PRAGMA table_info({table_name});")
        # Wrap table name in double quotes to handle spaces
        self.cursor.execute(f'PRAGMA table_info("{table_name}");')
        schema = self.cursor.fetchall()
        return schema
    
    def get_create_statement(self, table_name):
        # Get CREATE statement for the table
        self.cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        create_statement = self.cursor.fetchone()
        if create_statement:
            return create_statement
        else:
            print(f"No CREATE statement found for table '{table_name}'")

    def run_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result



        

