import streamlit as st
import pickle as pkl
import numpy as np

st.title("Model Prediction")
st.write('Linear Regression perform more accurately than other models. Therefore we use Linear Regression for prediction.')
st.image("sales_pred.png")
    
x1 = st.slider("Average session Length : ",min_value=25.0,max_value=100.0,step=.1,value=30.0 )
    
x2 = st.slider("Time spent on App : ",min_value=8.0,max_value=80.0,step=0.1,value=15.0)
    
x3 = st.slider("Time spent on Website : ",min_value=30.0,max_value=80.0,step=0.1,value=30.0)
    
x4 = st.slider("Length of Membership : ",min_value=0.1,max_value=10.0,step=0.001,value=1.00)
    
model = pkl.load(open('Linear.pkl','rb'))
    
if st.button('Predict Sale'):
    x = model.predict(np.array([[x1,x2,x3,x4]]))[0]
    st.write("Predicted Yearly Amount Spent : "+ str(x))
        

