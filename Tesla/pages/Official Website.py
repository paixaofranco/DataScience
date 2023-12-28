import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
#components.iframe("https://www.tesla.com")
#st.markdown('<a href="https://www.tesla.com" target="_self">WEBSITE</a>', unsafe_allow_html=True)

st.link_button("Go to TESLA.COM", "https://www.tesla.com")