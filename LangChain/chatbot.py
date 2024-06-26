import os
import streamlit as st
from langchain.chat_models import ChatOpenAI

from api import API_KEYS

st.set_page_config(page_title="무엇이든 질문하세요 !")
st.title("무엇이든 질문하세요 !")

os.environ["OPENAI_API_KEY"] = API_KEYS["OPENAI"]

def generate_response(input_text):
    llm = ChatOpenAI(temperature=0,
                     model_name='gpt-4'
                     )
    
    st.info(llm.predict(input_text))
    

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?')
    
    submitted = st.form_submit_button('보내기')
    
    generate_response(text)