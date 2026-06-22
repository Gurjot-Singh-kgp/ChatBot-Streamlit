# Streamlit Chatbot using Groq

A simple AI chatbot built using:
- Streamlit
- Groq API
- OpenAI SDK

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Create a `.env` file

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_key_here
```

## Run the application

```bash
streamlit run app.py
```

## Project Structure

```text
.
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── chatgpt-ui-streamlit.py
```

## Features

- Interactive chat interface
- Conversation history
- Adjustable temperature parameter
- Adjustable max token parameter
- Streaming responses
- Powered by Groq LLMs

### Model

- llama-3.3-70b-versatile
