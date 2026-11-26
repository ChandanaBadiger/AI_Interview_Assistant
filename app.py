
import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant', layout='centered')
st.title('🎯AI interview Assistant')
st.caption('practice interviews with AI-generated questions and constructive feedback')
st.caption('Launched by ChandanaBadiger')
st.write('Department of AI&DS')
try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write('API CONNECTION SUCCESSFUL')
except (KeyError,FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud -> App Setting Secrets')
  st.stop()

role = st.selectbox("Select Job Role",[
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Machine learning Engineer",
  "Software Engineer",
  "HR Executive"
])
if st.button("Generate Interview Questions"):
  prompt = "Generate 5 interview questions for the role of " + role
  response = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
              {"role" : "system", "content" : "you are an expert technical interviewer"},
          {"role": "user", "content": prompt}
      ]
  )
  output = response.choices[0].message.content
  st.write(output)
