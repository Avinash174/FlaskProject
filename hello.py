import streamlit as st
import seaborn as sns
st.write("Hello Avinash , Welcome In Streamlit") # for output msg
name_movie=st.text_input('Favourite Movie')
st.write(f"Your favourite movie is {name_movie}")
df=sns.load_dataset('iris')
st.write(df)
st.bar_chart(df)
is_click=st.button("Click Me")