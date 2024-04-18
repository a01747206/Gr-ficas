import streamlit as st
import pandas as pd

st.title("Titanic App")
st.header("Titanic Graphs - App")
st.write("Gráficas del dataset Titanic")

titanic_link = "Titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)