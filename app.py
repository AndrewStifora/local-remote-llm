from langchain_openai import ChatOpenAI
import streamlit as st
import os

# Environment Variables
OPENROUTER_API_KEY = "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"
REMOTE_MODEL_NAME = "qwen/qwen3-30b-a3b"
REMOTE_BASE_URL = "https://openrouter.ai/api/v1"

cloud_llm = ChatOpenAI(
    model = REMOTE_MODEL_NAME,
    api_key = OPENROUTER_API_KEY,
    base_url = REMOTE_BASE_URL
)

##############################################################

st.title("Talk to me...")

st.session_state.setdefault(
    "messages",
    []
)

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": prompt
        }
    )
    with st.chat_message("user"):
        st.write(prompt)
        
    context = ""
    
    for msg in st.session_state["messages"]:
        context += msg["role"] + ": " + msg["content"]
        
    response = cloud_llm.invoke(context)
    
    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": response.content
        }
    )
    
    with st.chat_message("assistant"):
        st.write(response.content)
