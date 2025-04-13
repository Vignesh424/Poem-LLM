#Import Packages

import streamlit as st
import traceback
import os
import google.generativeai as genai 
from dotenv import *

#Get API_key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))



#Function to generate a Poem
def google_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0],question])
    return response.text


#Prompt

prompt = ["""
          
You are an expert Poet. The question will like for example
          1. Recite a poem on Machine Learning 
          2. Draft a poem on 13th day of Mahabharata War
          Your job is to generate a poem after clearing the cache
          """]

#Streamlit App
st.title('Poem Generator')
question = st.text_input('On which topic you want the peom to be generated?', key='input_text')
if "input_text" not in st.session_state:
    st.session_state.question = ""
submit = st.button('Submit')
clear = st.button('Clear')

if submit:
    try:
        response = google_gemini_response(question,prompt)
        st.subheader('Generated Response')
        st.write(response)
    
    except Exception as e:
        print('Error generated. Try again')
        traceback.print_exc()

if clear:
    st.session_state.question = ""
    st.success('Cleared')


