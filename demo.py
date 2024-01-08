import streamlit as st
st.set_page_config(page_title='Dumb')
st.header("Presenting...")

col1,col2 = st.columns(2)
with col1:
  st.subheader("Girl")
  st.image("https://i.pinimg.com/736x/10/82/d7/1082d763e8eb696484449d20ae7578b9.jpg", caption="Gurl", width=300, use_column_width=True)
  st.write("Girls are cute")
  
with col2:
  st.subheader("Boy")
  st.image("https://i.pinimg.com/736x/10/82/d7/1082d763e8eb696484449d20ae7578b9.jpg", caption="Boi", width=300, use_column_width=True)
  st.write("Boys are Potatoes")
