import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("Hate Speech Classification with GPT-3.5 Turbo")

# Streamlit input for user text
user_input = st.text_area("Enter text for hate speech classification:")

# Function to classify hate speech using GPT-3.5 Turbo
def classify_hate_speech(text):
    # Replace "your_engine_id" with the ID of the GPT-3.5 Turbo engine
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 Turbo engine
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None
    )
    
    # Get the generated text from the response
    generated_text = response['choices'][0]['text']
    
    return generated_text

# Check if the user has entered text
if user_input:
    # Classify hate speech using GPT-3.5 Turbo
    classification_result = classify_hate_speech(user_input)
    
    # Display the results
    st.subheader("Classification Result:")
    st.write(classification_result)
else:
    st.info("Please enter text for hate speech classification.")
