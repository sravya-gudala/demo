import streamlit as st
st.set_page_config(page_title='Magic')
st.header("Hogwarts")

col1,col2 = st.columns(2)
with col1:
  st.subheader("Gryffindor")
  st.image("https://i.pinimg.com/originals/81/7d/36/817d3670dbdf4a263893c476bcda0ca3.jpg", caption="Harry Potter", width=300, use_column_width=True)
  st.write("Shut up, Malfoy!")
  
with col2:
  st.subheader("Slytherin")
  st.image("https://img.freepik.com/premium-vector/vector-chibi-draco-malfoy_969040-25.jpg", caption="Draco Malfoy", width=300, use_column_width=True)
  st.write("ooh Dementor! Dementor!")
