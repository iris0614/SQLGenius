# SQL Genius 🚀

This project is a SQL query agent application that uses OpenAI's language model to interpret and execute SQL queries on a user-uploaded database. The application is built with [Streamlit](https://streamlit.io/), providing an interactive interface for users to:

- Upload a `.db` file (or use one of several sample databases).  
- Run SQL queries by typing either SQL commands or natural language questions.  
- Display query results in an interactive table and optionally download them as `.csv`.
  
You can access the live app here: [SQL Genius](https://sqlgenius20250212.streamlit.app/).

---

## Features ✨

1. **Flexible Database Upload** 📂  
   - Easily upload and query your own SQLite `.db` file.  
   - Preloaded with sample databases like `Chinook.db`, `Northwind.db`, and `VitalDB.db` for quick testing.

2. **AI-Powered Query Generation** 🤖  
   - Enter **natural language questions** or **SQL**.  
   - The app uses OpenAI's language model to interpret and translate your request into a valid SQL query, then executes it.

3. **Results Display & Download** 📊  
   - Query results are displayed in a streamlined, interactive table with **AgGrid**.  
   - Download your results as a `.csv` file directly from the app.

4. **Privacy & Safety Checks** 🔒  
   - Optional **sensitive database** mode to restrict queries that expose personally identifiable or confidential information.  
   - Only read-only queries are allowed (SELECT, CREATE VIEW) unless configured otherwise.

5. **Error Handling** ❗  
   - Friendly alerts for invalid queries, missing columns, or issues with database connections or AI responses.

---

## Prerequisites 🛠️

- **Python 3.7 or higher** 🐍  
- **[Streamlit](https://streamlit.io/)**  
- **[OpenAI API Key](https://platform.openai.com/account/api-keys)** 🔑  
- Required Python libraries listed in `requirements.txt` (e.g., `pandas`, `numpy`, `st_aggrid`, etc.)

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:iris0614/SQLGenius.git
   cd SQLGenius
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory with your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```


1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

After a moment, Streamlit will open a new tab in your browser (usually at `http://localhost:8501`).

---

## Example Workflow🛠️

1. **Select or Upload a Database**  
   - For instance, choose `Northwind.db`.

2. **Ask a Question (SQL Query area)**  
   - Example:  
     ```
     Which UK customers have paid us more than 1000 dollars?
     ```

3. **Click "Execute SQL Query"**  
   - The AI will generate and run the SQL.  
   - Results (number of customers by country) are shown in a table.

---

## Troubleshooting🚑

- **Database Upload Errors**: Ensure your `.db` file is a valid SQLite database.  
- **OpenAI API Errors**: Double-check that your API key is correct and has sufficient permissions/credits.  
- **No Results Returned**: Check your SQL query logic or verify that relevant data is present in your database.  

---

## Data Sources📚

### VitalDB

The `medical_database.db` file (or `VitalDB.db`) used in this application is based on **VitalDB**, a high-fidelity multi-parameter vital signs database for surgical patients. The dataset, contributed by Hyung-Chul Lee and Chul-Woo Jung, provides comprehensive vital signs information valuable for research and analysis.

- **Dataset Title**: VitalDB  
- **Contributors**: Hyung-Chul Lee, Chul-Woo Jung  
- **Version**: 1.0.0  
- **Publication Date**: September 21, 2022  
- **License**: Creative Commons Attribution 4.0 International Public License (CC BY 4.0)

The dataset can be freely used, distributed, and modified as long as appropriate credit is given to the original authors. For more information, refer to the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).

---

## License📜

This project is licensed under the [MIT License](LICENSE).  


