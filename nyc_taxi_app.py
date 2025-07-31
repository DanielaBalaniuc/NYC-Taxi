import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_parquet("your_dataset.parquet")
    return df

st.title("NYC Taxi Data Explorer")

df = load_data()
st.write("Sample of the data:", df.head())
