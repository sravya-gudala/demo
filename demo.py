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
  st.image("https://img.wattpad.com/b33d61c84b3f4759d14ff66d36687fee6172c5ad/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f5a556249646955725f78386d54773d3d2d3139302e313634633831393963636134623534373138373537393133313830332e6a7067?s=fit&w=720&h=720", caption="Draco Malfoy", width=300, use_column_width=True)
  st.write("ooh Dementor! Dementor!")
