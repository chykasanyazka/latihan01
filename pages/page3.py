import streamlit as st
import pandas as pd

st.title("Settings")
st.write("This page allows you to customize your preferences.")

df = pd.read_csv('data/datakopikenangan.csv')
st.write(df.tail())

st.write("Simulasi error")