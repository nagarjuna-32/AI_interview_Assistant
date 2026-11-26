import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI INTERVIEW ASSISTANT', layout='centered')
st.title('AI INTERVIEW ASSISTANT')
st.caption('Practice interviews with AI-generated questions and constructive feedback.')
st.caption('Launched by CHANDRAKANTH.')
st.write("Depatment of aids")

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection succesful")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud -> App setting secrets')
  st.stop()

import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Interview Assistant")

role = st.selectbox("Select Job Role",[
  "Python Developer",
  "Data Analyst",
  "Machine Learning Engineer",
  "Software Engineer",
  "HR Executive"
])

if st.button("Generate Interview Questions"):
  prompt = "Generate 5 interview questions for the role of " + role
  response = client.chat.completions.create(
    model= "qwen/qwen3.8-27b",
    messages= [
        {"role": "system", "content": "You are an Expert Technical Interviewer."},
        {"role": "user", "content": prompt}
    ]
    )
  output = response.choices[0].message.content
  st.write(output)
