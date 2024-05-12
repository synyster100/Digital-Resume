from pathlib import Path
import streamlit as st
from PIL import Image

if "__file__" in locals():
    cd=Path(__file__).parent 
else: 
    Path.cwd()

css = cd/"styles"/"main.css"
resume = cd/"assets"/"Resume.pdf"
profile = cd/"assets"/"dp.jpg"


# --- General---
page_title= "Digital Resume | Tawkir Arifin"
page_icon=":wave:"
name="Tawkir Arifin"
description = """A beginning web developer and a great musician"""
email= "tawkirarifin200@gmail.com"
phone= "01946282670"
social = {"facebook": "https://www.facebook.com/tawkir.arifin.9/", "linkedin": "https://www.linkedin.com/in/tawkir-arifin-310a00230/", "github": "https://github.com/synyster100", }
project={"Medihome": "https://github.com/synyster100/Medihome","Games": "https://github.com/synyster100/PY-projects-" }

st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title("Resume of Tawkir Arifin")

# -- load css pdf and jpg---
with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume, 'rb') as pdf_file:
    PDFbyte=pdf_file.read()  
profile=  Image.open(profile)    

#--- hero section---
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile,width=230)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(label="Download Resume", data="PDFbyte",file_name=resume.name,mime="application/octate-stream")
    st.write("Email: ",email)
    st.write("Phone: ",phone)

#--- social links---
st.write('#')
cols= st.columns(len(social))
for index, (platform,link) in enumerate(social.items()):
    cols[index].write(f"[{platform}]({link})")

#--- Experience & Qualifications ---
st.write('#')
st.subheader("Experience & Qualifications")
st.write(
    """
    - Created a online medicine delivery system using HTML, CSS, PHP
    - Organizer of National Science Olympiad
    - Strong hands on HTML, CSS ,python
    - Excellent team player 
    - Keyboard artist in band Waffles but Pancakes

    """)
# --- Skills ---
st.write('#')
st.subheader("Skills")
st.write(
    """
    - Good in HTML, CSS
    - Programming: Python, SQL, PHP
    - Expert in MS word, MS excel, MS powerpoint
    - Database: MySQL, MongoDB
    - Webdev Framework: Flask, Django, streamlit

    """) 

# --- Work history --- 
st.write("#")
st.subheader("Work History")
st.write("---")

#here will be the job descriptions 
st.write("#")
st.write("job title")
st.write("job date")
st.write("Job description")

#--- Projects and achievements ---
st.write("#")
st.subheader("Projects and achievements")
st.write("---") 
for project,link in project.items():
    st.write(f"[{project}]({link})")     