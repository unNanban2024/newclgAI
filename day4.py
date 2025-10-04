import streamlit as st
from google import genai
chitti = genai.Client(api_key="AIzaSyCVOT7MTWxCZQ10kcTweeDx01kla_cKKIA")

st.title("My Own chatGPT")

question = st.text_input("Ask Anything")

if st.button("Send"):
    response = chitti.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question
        )
    
    st.write(response.text)
