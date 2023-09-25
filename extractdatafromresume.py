import streamlit as st

import PyPDF2
import docx
from io import BytesIO

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    pdf_content = pdf_file.read()
    pdf_file = BytesIO(pdf_content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)  # Use PdfReader instead of PdfFileReader
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

# Function to extract text from a Word document
def extract_text_from_docx(docx_file):
    docx_text = ""
    docx_content = docx_file.read()
    docx_file = BytesIO(docx_content)
    doc = docx.Document(docx_file)
    for paragraph in doc.paragraphs:
        docx_text += paragraph.text + '\n'
    return docx_text

# Streamlit UI
st.title("Resume Data Extractor")

uploaded_resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_resume is not None:
    file_type = uploaded_resume.type

    if file_type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_resume)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_resume)

    st.subheader("Extracted Text from Resume:")
    st.text(resume_text)
