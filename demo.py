import streamlit as st
st.set_page_config(page_title='Dumb')
st.header("Presenting...")

col1,col2 = st.columns(2)
with col1:
  st.subheader("Girl")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fcute-anime-chibi-little-girl-cartoon&psig=AOvVaw3MJbPLSqgf14GIim0X5aVq&ust=1704782388363000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJCrprqXzYMDFQAAAAAdAAAAABAD", caption="Persian Cat", width=300, use_column_width=True)
  st.write("Girls are cute")
  
with col2:
  st.subheader("Boy")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F843932417677448727%2F&psig=AOvVaw01OmLvUGSSnZj5beL1RN-C&ust=1704782486855000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJDb9O6XzYMDFQAAAAAdAAAAABAD", caption="Ragdoll Cat", width=300, use_column_width=True)
  st.write("Boys are Potatoes")
