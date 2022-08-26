import streamlit as st
import pandas as pd


tab1, tab2, tab3 = st.tabs(['Linear Regression','Decision Tree','Random Forest'])

with tab1:
    st.header("Linear Regression")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[0.9854,0.9778,8.5584,109.8637,10.4815]})
    st.dataframe(dt)

with tab2:
    st.header("Decision Tree")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[1.0,0.8515,21.60,734.9773,27.11]})
    st.dataframe(dt)
    

with tab3:
    st.header("Random Forest")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[0.9920,0.9345,13.9063,323.1598,17.9766]})
    st.dataframe(dt)
    
    

