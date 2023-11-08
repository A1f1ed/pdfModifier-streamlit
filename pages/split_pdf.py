import streamlit as st
import PyPDF2
import zipfile,os,tempfile
import base64

st.subheader("Select the file you want to split")
uploaded_file = st.file_uploader('file select',type=['pdf'],accept_multiple_files=False,label_visibility="hidden")

# create a temporary directory for storage
temp_dir = tempfile.mkdtemp()
file_paths = [] 
if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)


    # create pdf writer for output files
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)
        
        # write this to file
        
        saved_file_path = os.path.join(temp_dir,f"page_{page_num+1}.pdf")
        file_paths.append(saved_file_path)
        with open(saved_file_path,"wb") as output_file:
            pdf_writer.write(output_file)

    # create an archive
    zip_name = "splitted_pdf.zip"
    with zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            zipf.write(file_path,os.path.basename(file_path))
            
    with open(zip_name, "rb") as zip_file:
        zip_data = zip_file.read()
        st.download_button(label="Download", data=zip_data, key="download-zip",on_click=None, file_name="splitted_pdf.zip")