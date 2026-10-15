import streamlit as st
from chatbot import get_answer

# Page title
st.set_page_config(
    page_title="AI/ML FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI/ML Learning FAQ Chatbot")
st.write("Ask me questions about Artificial Intelligence and Machine Learning!")

# User input
user_question = st.text_input("Enter your question:")

# Get answer
if st.button("Ask"):
    if user_question.strip():
        answer = get_answer(user_question)
        st.success(answer)
    else:
        st.warning("Please enter a question.")