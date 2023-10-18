import streamlit as st

st.set_page_config(page_title="Layout", layout='wide')
st.title('streamlit layout')

sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')

col1, col2, col3 = st.columns(3)

with col1:
    st.write('this is col 1')
    st.image('./media/cat.jpg')

with col2: 
    st.write('this is col 2') 
    st.image('./media/dog.jpg')

with col3:
    st.write('this is col 2')
    st.image('./media/owl.jpg')

st.header('display in tabs')

tab1, tab2, tab3 = st.tabs(['cat', 'dog', 'owl'])

with tab1:
    st.write('this is tab 1')
    st.image('./media/cat.jpg')

with tab2:
    st.write('this is tab 2')
    st.image('./media/dog.jpg')

with tab3:
    st.write('this is tab 3')
    st.image('./media/owl.jpg')

