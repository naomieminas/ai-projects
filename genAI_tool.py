import streamlit as st
from transformers import pipeline

# Load the AI model #
AI = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Streamlit Formatting
st.title("GatesAI")

st.markdown("Welcome to GatesAI! Ever wanted to chat with a multi-billionaire tech titan? Well, now you can! Pick the mind \
of Bill Gates, founder of Microsoft and Chair of the Bill and Melinda Gates Foundation. Ask him all about the climate \
crisis or make fun of him for dropping out, the choice is yours!")

question = st.text_input("Ask me a question: ")

if st.button("Ask"):
    result = AI(question = question)
    st.write(result['answer'])
