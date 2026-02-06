import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trading Bot Dashboard", layout="wide")
st.title("📊 Trading Bot Dashboard")

st.metric("Account Balance", "$500")
st.metric("Drawdown", "2%")
st.metric("Trades Today", "3")

st.subheader("Performance")
st.line_chart(pd.DataFrame({"equity":[500,510,505,520]}))
