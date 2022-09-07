import streamlit as st
import pandas as pd


tab1, tab2, tab3 = st.tabs(['Linear Regression','Decision Tree','Random Forest'])

with tab1:
    st.subheader("What is Linear Regression ?")
    st.write("""
    Linear regression is one of the easiest and most popular Machine Learning algorithms. It is a statistical method that is used for predictive analysis. Linear regression makes predictions for continuous/real or numeric variables such as sales, salary, age, product price, etc. 
    """)
    st.write("""
    Linear regression algorithm shows a linear relationship between a dependent (y) and one or more independent (x) variables, hence called as linear regression. The linear regression model provides a sloped straight line representing the relationship between the variables
    """)
    st.image('linear_regression.png')
    st.subheader("Model Performance")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[0.9854,0.9778,8.5584,109.8637,10.4815]})
    st.dataframe(dt)

with tab2:
    st.subheader("What is Decision Tree ?")
    st.write("""
    Decision Tree is one of the most commonly used, practical approaches for supervised learning. It can be used to solve both Regression and Classification tasks with the latter being put more into practical application.
    """)
    st.write("""
    It is a tree-structured classifier with three types of nodes. The Root Node is the initial node which represents the entire sample and may get split further into further nodes. The Interior Nodes represent the features of a data set and the branches represent the decision rules. Finally, the Leaf Nodes represent the outcome.
    """)
    st.image('decision_tree.png')
    st.subheader("Model Performance")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[1.0,0.8515,21.60,734.9773,27.11]})
    st.dataframe(dt)
    

with tab3:
    st.subheader("What is Random Forest ?")
    st.write("""
    Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression. 
    """)
    st.write("""
    Ensemble simply means combining multiple models. Thus a collection of models is used to make predictions rather than an individual model. Random forest uses Bagging mehod. This method creates a different training subset from sample training data with replacement & the final output is based on majority voting.
        """)
    st.image('random_forest.png')
    st.subheader("Model Performance")
    dt = pd.DataFrame({'Metrics':['Training r2 Score','Testing r2 Score','MAE','MSE','RMSE'],'Value':[0.9920,0.9345,13.9063,323.1598,17.9766]})
    st.dataframe(dt)
    
    

