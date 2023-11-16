import streamlit as st
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("Hate Speech Classification")

user_input = st.text_area("Enter text for hate speech classification:")

def classify_hate_speech(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": text},
        ],
    )
    return completion.choices[0].message['content']

if st.button("Submit"):
    if user_input:
        classification_result = classify_hate_speech(user_input)

        st.subheader("Classification Result:")
        st.write(classification_result)
    else:
        st.warning("Please enter text for hate speech classification.")
