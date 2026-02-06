import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trading Bot Dashboard", layout="wide")
st.title("📊 Trading Bot Dashboard")

try:
    df = pd.read_csv("journal.csv", header=None,
                     names=["Time", "Symbol", "Signal", "Price", "Qty"])
    st.dataframe(df)
    st.metric("Total Trades", len(df))
except FileNotFoundError:
    st.warning("Aún no hay operaciones registradas.")
