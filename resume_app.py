import os
import streamlit as st
from RESUME_UPDATER import update_resume  # Import your update function

# Streamlit App
st.title("📄 AI Resume Updater")
st.write("Upload your resume and paste the job description to get a tailored resume.")

# Resume file upload
uploaded_file = st.file_uploader("Upload your Resume (in .txt format)", type=["txt"])

# Job description input
job_description = st.text_area("Paste Job Description", height=200, placeholder="Enter the job requirements here...")

# Create output directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

if st.button("Update Resume"):
    if uploaded_file is not None and job_description.strip():
        # Save uploaded resume temporarily
        resume_path = os.path.join(OUTPUT_DIR, uploaded_file.name)
        with open(resume_path, "wb") as f:
            f.write(uploaded_file.read())

        # Call your function
        updated_resume = update_resume(resume_path, job_description)

        # Save updated resume
        updated_resume_file = os.path.join(OUTPUT_DIR, "updated_resume.txt")
        with open(updated_resume_file, "w", encoding="utf-8") as f:
            f.write(updated_resume)

        st.success("✅ Resume updated successfully!")
        st.download_button(
            label="📥 Download Updated Resume",
            data=updated_resume,
            file_name="updated_resume.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Please upload a resume and provide a job description.")
