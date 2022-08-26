import streamlit as st
import pandas as pd

st.title("Data Description")
st.write('This dataset is having data of customers who buys clothes online. The store offers in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.')

df = pd.read_csv('/content/drive/MyDrive/E_Commerce_Sales/sample_new.csv')
    
st.dataframe(df.head())
