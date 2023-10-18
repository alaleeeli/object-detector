import streamlit as st

st.write('Hello world')

st.header("This is a header")

st.subheader("This is a subheader")

st.caption('This is a caption')
st.text('This is plain text')

# markdown

st.markdown("""
# this is a title
## This is header
            
simple plain text
for *italic*
for **bold**
""")

# status element
# success
st.success('This message display text in green')
# warning
st.warning('this message display text in yello')
# error
st.error('this message display text in red')

# display media
# image and video
st.subheader("display image")

st.image('./media/mountains.webp', caption='mountains')

st.subheader("display video")

video_file = open('./media/star.mp4', mode='rb').read()
st.video(video_file)



