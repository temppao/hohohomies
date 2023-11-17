import streamlit as st
import openai
import os

def main():
    tabs = ["Home", "Project Overview", "Application"]
    selected_tab = st.sidebar.selectbox("Select a Page", tabs)

    if selected_tab == "Home":
        home_content()
    elif selected_tab == "Project Overview":
        overview_content()
    elif selected_tab == "Application":
        app_content()

def home_content():
    st.markdown("<h1 style='text-align: center;'>Welcome to The Ho-Ho-Homies Streamlit App!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This app is created for Eskwelabs DSF12 Sprint 4 by The Ho-Ho-Homies</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please use the sidebar to navigate the page.</p>", unsafe_allow_html=True)

def overview_content():
    st.title("Project Overview")

def app_content():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    st.title("Hate Speech Identification App")
    
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
            prompt = f"Consider this statement: {user_input}\n\
                Please identify whether this statement is hate speech or not. If it is hate speech, please classify what kind of hate speech it is (examples are racism, sexism, religious bias, etc.)\
                The output should look exactly like this. The output should look exactly like this\n\
                This is an example of hate speech. This can be classified as racism."
            classification_result = classify_hate_speech(prompt)
    
            st.subheader("Classification Result:")
            st.write(classification_result)
        else:
            st.warning("Please enter text for hate speech classification.")
            
if __name__ == "__main__":
    main()
