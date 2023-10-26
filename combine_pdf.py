import streamlit as st
import PyPDF2

st.subheader("Select the files in the order you want them to merge")
file_list = st.file_uploader(' ',type=['pdf'],accept_multiple_files=True)

# get the list of file names
if file_list:
    # for file in file_list:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line)

    # file_names = [file.name for file in file_list]
    # print(file_names)
    # # create a pdf reader for the input files
    # pdf_reader_list=[]
    # for file in file_names:
    #     read_file = PyPDF2.PdfFileReader(open(file,"rb"))
    #     print(file,'read')
    pdf_reader_list  = [PyPDF2.PdfReader(open(file.name,"rb")) for file in file_list]

    # create a pdf writer for the output files
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_reader in pdf_reader_list:
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # # write the combined result to a file
    with open("combined.pdf","wb") as output_file:
        pdf_writer.write(output_file)
    
    st.text("Done! check downloads")
