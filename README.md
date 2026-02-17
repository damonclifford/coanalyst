# 🤖 coanalyst.ai

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0.3-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)](https://openai.com/)

**Transform your data into insights with natural language queries powered by AI**

[Visit Website](http://www.coanalyst.ai) • [Report Bug](https://github.com/damonclifford/coanalyst/issues) • [Request Feature](https://github.com/damonclifford/coanalyst/issues)

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About

**coanalyst.ai** is an intelligent data analysis application that leverages the power of AI to make data exploration accessible to everyone. Simply ask questions about your data in plain English, and get instant SQL queries and insights powered by OpenAI's GPT models.

No need to write complex SQL queries or understand database structures - coanalyst.ai translates your natural language questions into executable SQL and provides human-readable analysis of the results.

### Why coanalyst.ai?

- 🚀 **No SQL Knowledge Required** - Ask questions in plain English
- 🧠 **AI-Powered Analysis** - Leverages OpenAI's GPT models for intelligent query generation
- 📊 **Instant Insights** - Get immediate answers to your data questions
- 🎨 **Modern UI** - Beautiful, responsive interface built with Bootstrap 5
- 🔧 **Easy to Use** - Simple setup and intuitive workflow

---

## ✨ Features

### Current Features

- 💬 **Natural Language Queries** - Ask questions about your data in plain English
- 🤖 **AI-Powered SQL Generation** - Automatically converts questions to SQL queries
- 📈 **Intelligent Analysis** - Provides natural language explanations of query results
- 🗂️ **CSV Data Support** - Analyze data from CSV files (currently using UCI Online Retail Dataset)
- 🎯 **Query Suggestions** - Pre-built example questions to get started quickly
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🔍 **Data Preview** - View sample data before querying

### Example Queries

- "What was the total revenue?"
- "What were the top two stores and their sales?"
- "Who was the top customer?"
- "How much did the Miami store sell?"
- "What is the average order value?"
- "Which products sell the most by quantity?"

---

## 🎬 Demo

The application features a modern, intuitive interface where users can:

1. **Enter natural language questions** about their data
2. **View automatically generated SQL queries** that answer their questions
3. **Read AI-powered analysis** of the results in plain English

The interface includes:
- Beautiful gradient hero section
- Interactive suggestion cards for common queries
- Data preview table showing sample records
- Results section displaying the question, generated SQL, and AI analysis

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager) - Usually comes with Python
- **OpenAI API Key** - [Get your API key](https://platform.openai.com/account/api-keys)

---

## 🚀 Installation

Follow these steps to get coanalyst.ai running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/damonclifford/coanalyst.git
cd coanalyst
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The application requires the following packages:
- `openai==0.10.5` - OpenAI API client
- `pandas==1.5.3` - Data manipulation and analysis
- `Flask==2.0.3` - Web framework
- `SQLAlchemy~=1.4.46` - SQL toolkit and ORM
- `numpy==1.24.2` - Numerical computing

---

## ⚙️ Configuration

### Set Up Your OpenAI API Key

1. Open the `config.py` file in the root directory
2. Replace `'YOUR-OPENAI-API-KEY'` with your actual OpenAI API key:

```python
##OPEN API
OPENAI_API_KEY = 'sk-your-actual-api-key-here'
```

**⚠️ Security Note:** Never commit your actual API key to version control. Consider using environment variables for production deployments.

### Alternative: Using Environment Variables (Recommended)

For better security, you can use environment variables:

```bash
# On Windows
set OPENAI_API_KEY=sk-your-actual-api-key-here

# On macOS/Linux
export OPENAI_API_KEY=sk-your-actual-api-key-here
```

Then modify `config.py`:

```python
import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR-OPENAI-API-KEY')
```

---

## 💻 Usage

### Running the Application

1. Ensure your virtual environment is activated (if you created one)
2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and navigate to:

```
http://localhost:5000
```

### Using the Application

1. **Enter a Question** - Type your question about the data in the input field
2. **Try Example Questions** - Click any suggestion card to auto-fill example queries
3. **View Results** - After submitting, you'll see:
   - Your original question
   - The generated SQL query
   - AI-powered analysis of the results
4. **Reset** - Click the "Reset" button to clear the form and start over

### Working with Your Own Data

To use your own dataset:

1. Replace the CSV file in the `assets/` directory
2. Update line 21 in `app.py` to point to your CSV file:

```python
df = pd.read_csv('assets/your_data_file.csv')
```

3. Adjust the table definition in the `create_table_definition()` function if needed

---

## 📁 Project Structure

```
coanalyst/
│
├── app.py                  # Main Flask application
├── config.py              # Configuration file (API keys)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
│
├── assets/               # Data files
│   └── Online_Retail_1000_v2.csv
│
└── templates/            # HTML templates
    ├── index.html        # Main application interface
    └── 404.html          # Error page
```

### Key Files

- **app.py** - Core application logic including:
  - Flask routes and request handling
  - OpenAI API integration
  - SQL query generation and execution
  - Natural language response generation

- **config.py** - Configuration settings (API keys)

- **templates/index.html** - Frontend interface with:
  - Modern, responsive design
  - Interactive query suggestions
  - Results display
  - Data preview table

---

## 🛠️ Technologies

coanalyst.ai is built with the following technologies:

### Backend
- **[Python](https://www.python.org/)** - Programming language
- **[Flask](https://flask.palletsprojects.com/)** - Web framework
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[OpenAI API](https://openai.com/api/)** - AI-powered query generation and analysis

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with modern gradients and animations
- **JavaScript** - Interactivity
- **[Bootstrap 5](https://getbootstrap.com/)** - UI framework
- **[Font Awesome](https://fontawesome.com/)** - Icons
- **[Google Fonts](https://fonts.google.com/)** - Typography (Inter)

### Data
- **SQLite** - In-memory database for query execution
- **CSV** - Data storage format

---

## 🗺️ Roadmap

### Upcoming Features

- [ ] **Load Your Own Spreadsheet** - Upload custom CSV files through the interface
- [ ] **Data Visualizations** - Generate charts and graphs automatically
- [ ] **Data Warehouse Integration** - Connect to external databases (PostgreSQL, MySQL, etc.)
- [ ] **Export Results** - Download query results as CSV or JSON
- [ ] **Query History** - Save and revisit previous queries
- [ ] **Multi-table Support** - Analyze relationships between multiple datasets
- [ ] **Advanced Analytics** - Statistical analysis and trend detection
- [ ] **User Authentication** - Secure user accounts and saved queries
- [ ] **API Access** - RESTful API for programmatic access

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Guidelines

- Write clear, commented code
- Follow existing code style and conventions
- Test your changes thoroughly
- Update documentation as needed
- Be respectful and constructive in discussions

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2023 Damon Clifford

---

## 📞 Contact

**Damon Clifford**

- GitHub: [@damonclifford](https://github.com/damonclifford)
- Website: [coanalyst.ai](http://www.coanalyst.ai)
- Tools: [AI Content Tools](https://www.contentgeneration.io/)

**Project Link:** [https://github.com/damonclifford/coanalyst](https://github.com/damonclifford/coanalyst)

---

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT models
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) for the Online Retail Dataset
- [Bootstrap](https://getbootstrap.com/) for the UI framework
- [Flask](https://flask.palletsprojects.com/) for the web framework
- All contributors who help improve this project

---

<div align="center">

**Made with ❤️ by Damon Clifford**

⭐ Star this repo if you find it useful!

</div>
