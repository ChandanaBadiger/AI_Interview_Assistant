import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant', layout='centered')
st.title('🎯AI interview Assistant')
st.caption('practice interviews with AI-generated questions and constructive feedback')
st.caption('Launched by ChandanaBadiger')
st.write('Department of AI&DS')
try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.caption('API CONNECTION SUCCESSFUL')
except (KeyError,FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud -> App Setting Secrets')
  st.stop()
