import streamlit as st
from utils import call_llm

st.set_page_config(page_title="TalentScout AI", layout="centered")
st.title("🤖 TalentScout - AI Hiring Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You: ", "")

# Process input
if user_input:
    response = call_llm(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")


