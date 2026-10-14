import streamlit as st

data = {
        1:"Ava",
        2:"Bob",
        3:"Carl",
        4:"Dale Cooper from Twin Peaks"
    }

input = st.text_input("Password:")

if input == "1234":
    st.table(data)