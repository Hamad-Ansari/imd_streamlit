#libraries
import streamlit as st
# imeage libraries 
from PIL import Image


# hadeing
st.write('''
            # Ai Work with every fielde in life
             ** Hammad Ansari**
            # Ai  us for imeage createion and editing and songe etc,
         ''')





#  add image
st.write("## Image")
imeage = Image.open('cat.img.jpg')
st.image(imeage, caption='cat', use_column_width=True)


# add video
st.write("## Video")
video_file = open('video.mp4', 'rb')
st.video(video_file, format='video/mp4')

#add voice
st.write("## Voice")
audio_file = open('song.mp3', 'rb')
st.audio(audio_file, format='audio/mp3')

# add file download
#st.write("## File Download")
#file_ = open('file.txt', 'rb')
#st.download_button(label='Download file', data=file_, file_name='file.txt', mime='text/plain')
#show the code
if st.checkbox('Show code'):
    with st.echo():
        #HAMMAD ANSARI
        st.write("## Voice")
        audio_file = open('song.mp3', 'rb')
        st.audio(audio_file, format='audio/mp3')

# add file upload
st.write("## File Upload")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])
if uploaded_file is not None:
    # To read file as string:
    string_data = uploaded_file.read().decode("utf-8")
    st.write(string_data)
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
    # To convert file to a string based on the file type:
    if uploaded_file.type == "text/plain":
        string_data = uploaded_file.read().decode("utf-8")
        st.write(string_data)
    elif uploaded_file.type == "application/pdf":
        pdf_data = uploaded_file.read()
        st.write(pdf_data)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        docx_data = uploaded_file.read()
        st.write(docx_data)
    else:
        st.write("Unsupported file type")
