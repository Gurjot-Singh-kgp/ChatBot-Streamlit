from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page title
st.title("Groq Chatbot")

# Initialize Groq client once
if "client" not in st.session_state:
    st.session_state["client"] = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar settings
st.sidebar.title("Model Parameters")

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=1,
    max_value=4096,
    value=512
)

# Display previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Enter your query"):

    # Store user message
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        client = st.session_state["client"]

        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state["messages"],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )

        response = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )

    # Store assistant response
    st.session_state["messages"].append(
        {"role": "assistant", "content": response}
    )