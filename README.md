# SQL Genius 🚀

A powerful SQL query agent application that leverages OpenAI's language model to interpret and execute SQL queries on user-uploaded databases. Built with Streamlit, it provides an intuitive interface for natural language to SQL query conversion and execution.

**Live Demo**: [SQL Genius](https://sqlgenius20250212.streamlit.app/)

> **Note**: This project builds upon and references the excellent work from [@yefan/tiny-sql-agent](https://github.com/yefan/tiny-sql-agent). We extend their core concepts with additional features and improvements.

---

## ✨ Key Features

### 🔍 **Intelligent Query Processing**
- **Natural Language to SQL**: Ask questions in plain English and get SQL queries automatically generated
- **Direct SQL Input**: Write and execute custom SQL queries directly
- **AI-Powered Translation**: OpenAI's language model handles complex query interpretation

### 📊 **Database Management**
- **Flexible Upload**: Upload your own SQLite `.db` files
- **Sample Databases**: Pre-loaded with `Chinook.db`, `Northwind.db`, and `VitalDB.db` for testing
- **Multiple Database Support**: Switch between different databases seamlessly

### 🎯 **Results & Export**
- **Interactive Tables**: Results displayed using AgGrid for enhanced user experience
- **CSV Download**: Export query results directly to CSV format
- **Real-time Updates**: Instant query execution and result display

### 🔒 **Security & Safety**
- **Read-Only Operations**: Default restriction to SELECT and CREATE VIEW operations
- **Privacy Protection**: Optional sensitive database mode for confidential data
- **Error Handling**: Comprehensive error messages and validation

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- OpenAI API Key
- Streamlit

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:iris0614/SQLGenius.git
   cd SQLGenius
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Launch the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

---

## 📖 Usage Guide

### Basic Workflow

1. **Select Database**
   - Choose from pre-loaded sample databases, or
   - Upload your own `.db` file

2. **Ask Your Question**
   - Type natural language questions like:
     ```
     Which UK customers have spent more than $1000?
     Show me the top 10 products by sales volume
     ```
   - Or write SQL queries directly

3. **Execute & View Results**
   - Click "Execute SQL Query"
   - View results in the interactive table
   - Download results as CSV if needed

### Example Queries

**Natural Language:**
```
"Find all employees who joined after 2010 and earn more than $50,000"
```

**Generated SQL:**
```sql
SELECT * FROM employees 
WHERE hire_date > '2010-01-01' AND salary > 50000
```

---

## 🗄️ Sample Databases

### Chinook Database
- Music store database with artists, albums, tracks, and sales data
- Perfect for learning SQL and testing queries

### Northwind Database
- Classic business database with customers, orders, products, and suppliers
- Great for business analytics and reporting examples

### VitalDB
- Medical database with patient vital signs and surgical data
- Based on research data from Hyung-Chul Lee and Chul-Woo Jung
- Licensed under Creative Commons Attribution 4.0 International

---

## 🛠️ Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| Database upload fails | Ensure file is a valid SQLite `.db` format |
| OpenAI API errors | Verify API key and check account credits |
| No query results | Review SQL logic or check database content |
| Connection issues | Restart the application and check database file |

### Getting Help
- Check that all dependencies are installed correctly
- Verify your OpenAI API key has sufficient permissions
- Ensure your database file is not corrupted

---

## 🔧 Technical Details

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: Python with OpenAI API integration
- **Database**: SQLite support with extensible architecture
- **Data Processing**: Pandas for data manipulation and display

### Dependencies
Key packages include:
- `streamlit` - Web application framework
- `openai` - OpenAI API client
- `pandas` - Data manipulation
- `st-aggrid` - Interactive table display
- `sqlite3` - Database operations

---

## 📚 Data Sources & Licensing

### VitalDB Attribution
The medical database used in this application is based on **VitalDB**, a high-fidelity multi-parameter vital signs database for surgical patients.

- **Dataset**: VitalDB v1.0.0
- **Contributors**: Hyung-Chul Lee and Chul-Woo Jung
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Publication**: September 21, 2022

### Project License
This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests to improve SQL Genius.

---

## 🙏 Acknowledgments

- **@yefan/tiny-sql-agent**: This project builds upon the foundational work and concepts from the [tiny-sql-agent](https://github.com/yefan/tiny-sql-agent) project
- **OpenAI**: For providing the language model capabilities
- **Streamlit**: For the excellent web application framework
- **Contributors**: All contributors who have helped improve this project


