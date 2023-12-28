import streamlit as st
import streamlit.components.v1 as components
pip install streamlit-modal
from streamlit_modal import Modal
import pandas as pd
import altair as alt
import plotly.express as px
import yfinance as yf


#######################
# Page configuration
st.set_page_config(
    page_title="Stock App",
    page_icon="<3",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################

st.write("""
# About this App
Built in December 2023 by """)
st.markdown('<a href="https://www.luyanafranco.com" target="_self">Luyana Franco</a>', unsafe_allow_html=True)

#############################

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input= st.text_input("What is your name?", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input


modal = Modal(key="Demo Key",title="Welcome!")
open_modal = submit
if open_modal:
    modal.open()
if modal.is_open():
    with modal.container():
        st.write("Hi ", my_input, ", I hope you enjoy this the app. From the side bar you can access stock movements and the official website.")
