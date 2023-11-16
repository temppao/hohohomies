import streamlit as st
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

prompt = "\n\nYou must classify the statement above whether it is hate speech or not. If the statement is not considered hate speech, you must output 'This is not an example of hate speech.'; however, if the example is considered hate speech, you must specify what kind of hate speech it is (examples: racism, sexism, religion, etc.), and you must output 'This is an example of hate speech. It is (insert type of hate speech).'"

st.title("Hate Speech Classification")

user_input = st.text_area("Enter text for hate speech classification:")

def classify_hate_speech(text):
    # Replace "your_engine_id" with the ID of the GPT-3.5 Turbo engine
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=text,
        n=1,
    )
    generated_text = response['choices'][0]['text']
    return generated_text

if user_input:
    text = user_input.join(prompt)
    classification_result = classify_hate_speech(text)

    st.subheader("Classification Result:")
    st.write(classification_result)
else:
    st.info("Please enter text for hate speech classification.")
