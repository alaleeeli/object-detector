import streamlit as st
import os

st.title('Input widgets')

st.header('button')

button = st.button('Button')

if button:
    st.write('You pressed on button')

st.header("checkbox")
checkbox = st.checkbox("Do you want to agree ?")

if checkbox:
    st.write('You check the box')

else:
    st.write('you unchecked')

options = ("uae", "ksa", "kwt")

radio = st.radio("what is your favorite country", options)

st.write('your favorite country is', radio)

options = ('email', 'phone', 'insta')

select_box = st.selectbox('How would you like to contact ?', options)

st.write('your prefered mode of communication is ', select_box)

slider_range = st.slider('How old are you', min_value=1, max_value=60, step=1, value=20)

st.write("your age is ", slider_range)

name = st.text_input('enter your name')

st.write('your name is ', name)

age = st.number_input('enter your age', min_value=1, max_value=100, step=1, value=20)

st.write('your age is ', age)

st.header('File upload')
uploader = st.file_uploader('Choose a File')

if uploader is not None:
    st.success('File uploaded successfully')
    details = {'filename': uploader.name,
               'filetype': uploader.type,
               'filesize (bytes)': uploader.size}
    
    st.json(details)

path = os.path.join('./upload', uploader.name)

with open(path, mode='wb') as f:
    f.write(uploader.getbuffer())
    st.success('File saved successfully')