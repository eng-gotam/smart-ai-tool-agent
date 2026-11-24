# 🤖 Specialized AI Tool Agent

An intelligent AI-powered agent that uses Google Gemini and automatic function calling to perform specialized tasks through external Python tools.

The application demonstrates practical AI engineering concepts, including multi-tool execution, scope restriction, error handling, and response latency monitoring.

## 🚀 Features

- Automatic tool selection using Gemini LLM
- Multiple tool execution within a single request
- Mathematical calculations
- Real-time date and timezone information
- Word and character analysis
- Basic AI guardrails for unsupported requests
- Automatic retry mechanism for server errors
- Tool execution tracking
- Response time monitoring
- Interactive Streamlit interface with dark theme

## 🛠️ Available Tools

| Tool | Functionality |
|---|---|
| Calculator | Addition, subtraction, multiplication, division and power |
| DateTime | Current date, time, day and timezone information |
| Text Analyzer | Word count and character analysis |

## 🏗️ System Architecture

```text
User Request
     |
Streamlit Interface
     |
Gemini LLM + System Instructions
     |
Automatic Tool Selection
     |
     +-- Calculator
     +-- DateTime
     +-- Text Analyzer
     |
Tool Results
     |
LLM Response
     |
Basic Output Guardrail
     |
Final Response
```

## ⚙️ Tech Stack

- Python
- Google Gemini API
- Google GenAI SDK
- Streamlit
- Python-dotenv
- ZoneInfo and tzdata
- Git and GitHub

## 📂 Project Structure

```text
smart-ai-tool-agent/
│
├── .streamlit/
│   └── config.toml
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── datetime_tool.py
│   └── text_tool.py
│
├── agent.py
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/eng-gotam/smart-ai-tool-agent.git
cd smart-ai-tool-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key from Google AI Studio:

https://aistudio.google.com/apikey

Never commit your API key to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

For terminal-based testing:

```bash
python agent.py
```

## 🧪 Example Prompts

- Multiply 25 by 40.
- What is the current time in Karachi?
- Count the words in "AI is powerful".
- Divide 100 by 0.
- Multiply 25 by 40, retrieve the current time in Karachi, and count the words in "AI is powerful".

The agent rejects unrelated general knowledge questions.

## 📊 Testing Results

The following results were recorded during local functional testing.

| Test Case | Response Time | Result |
|---|---:|---|
| Scope restriction | 1.45s | Passed |
| Calculator | 2.05s | Passed |
| DateTime | 26.29s | Passed |
| Text Analyzer | 10.34s | Passed |
| Division by zero | 1.90s | Passed |
| Multiple tool execution | 2.48s | Passed |

**Functional tests passed: 6/6**

**Average response time: 7.42 seconds**

**Median response time: 2.27 seconds**

The DateTime test encountered a temporary API server error and successfully recovered through the retry mechanism. Response times may vary depending on API availability and network conditions.

## 🧠 AI Engineering Concepts

This project demonstrates:

- Large Language Model integration
- Automatic function calling
- Multi-tool orchestration
- System prompt engineering
- Basic AI guardrails
- Context-based tool tracking
- Fault tolerance
- Response latency monitoring
- Modular Python architecture

## ⚠️ Current Limitations

- Response latency depends on Gemini API availability.
- Tools may execute more than once during retries.
- Scope restriction uses basic prompting and output validation rather than production-grade intent validation.
- Chat history is displayed in the interface, but conversational memory is not implemented in the LLM.
- The agent supports only three specialized tools.

## 🔮 Future Improvements

- Structured intent classification
- More reliable tool execution validation
- Additional tools and external API integrations
- Conversational memory
- Advanced agent orchestration
- Comprehensive automated evaluation

## 👨‍💻 Author

**Gotam Kumar**

BS Artificial Intelligence  
Sindh Madressatul Islam University, Karachi

GitHub: https://github.com/eng-gotam

Interests: AI Engineering, Generative AI, LLMs, RAG and Agentic AI.

---

Built as a practical AI Engineering portfolio project to explore intelligent tool-based agents.