import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit app UI
st.set_page_config(page_title="Resume Tailor", layout="wide")
st.title("🎯 Resume Tailor with Gemini")

job_desc = st.text_area("Paste the Job Description", height=200)
resume = st.text_area("Paste Your Resume", height=300)

if st.button("Tailor Resume"):
    if not job_desc.strip() or not resume.strip():
        st.error("⚠️ Please provide both job description and resume")
    else:
        prompt = f"""
        You are an expert resume writer. Given the following job description and resume,
        tailor the resume to highlight the most relevant skills and experiences.
        Keep it professional, concise, and ATS-friendly.

        Job Description:
        {job_desc}

        Resume:
        {resume}
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        st.subheader("✨ Tailored Resume:")
        st.write(response.text)
