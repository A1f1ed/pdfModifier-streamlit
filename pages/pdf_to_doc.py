import streamlit as st
from pdf2docx import Converter

st.subheader("Select the file you want to convert to docx")
uploaded_file = st.file_uploader('file select',type=['pdf'],accept_multiple_files=False,label_visibility="hidden")

if uploaded_file:
    cv = Converter(uploaded_file.name)
    file_name = uploaded_file.name[:-4] + ".docx"
    cv.convert(file_name,start=0,end=None)
    cv.close()
    
    with open(cv,"rb") as file:
        file_data = file.read()
        st.download_button(label="Download", data=file_data, key="download-doc",on_click=None, file_name=file_name)

