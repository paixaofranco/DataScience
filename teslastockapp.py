# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:55:27 2022

@author: luyan
"""

# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import yfinance as yf


#######################
# Page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################

st.write("""
# Teslsa Stock Price Dashboard
Shown are the stock closing price and volume of Tesla!
""")

#define the ticker symbol
tickerSymbol = 'TSLA'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)