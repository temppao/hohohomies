import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set prompt
prompt = "You must classify the statement above whether it is hate speech or not. If the statement is not considered hate speech, you must output 'This is not an example of hate speech.'; however, if the example\
        is considered hate speech, you must specify what kind of hate speech it is (examples: racism, sexism, religion, etc.), and you must output 'This is an example of hate speech. It is (insert type of hate speech).'

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
    text = user_input.join(prompt)
    # Classify hate speech using GPT-3.5 Turbo
    classification_result = classify_hate_speech(text)
    
    # Display the results
    st.subheader("Classification Result:")
    st.write(classification_result)
else:
    st.info("Please enter text for hate speech classification.")
