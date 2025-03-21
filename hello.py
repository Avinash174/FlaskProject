import streamlit as st
st.write("Hello Avinash , Welcome In Streamlit") # for output msg
name_movie=st.text_input('Favourite Movie')
st.write(f"Your favourite movie is {name_movie}")
is_click=st.button("Click Me")