import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# ------------Load environment variables------------------
load_dotenv()

# ------------Set your Gemini API key securely-------------
os.getenv("GEMINI_API_KEY")

# ---------------Streamlit UI-------------------------------

st.set_page_config(page_icon="🤖", page_title='Chatbot')
st.title('Chatbot by Qirat Saeed ')
st.caption('By LiteLLM & Streamlit')
def main():
    user_input = st.text_input('Ask Anything....')
    if st.button("Ask"):
       try:
            response = completion(
            model= "gemini/gemini-2.0-flash",
            messages=[{"role": "user", "content": user_input}]
        )
            st.success(response['choices'][0]['message']['content'])
       except Exception as e:
           st.error(f'{e}')
           
main()