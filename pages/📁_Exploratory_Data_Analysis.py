import streamlit as st


st.title("Exploratory Data Analysis")
st.subheader("Pairplot of Input Features")
st.image('/content/drive/MyDrive/E_Commerce_Sales/final_pairplot.png')
st.subheader("Correlation of input feature with output feature")
selected_feature = st.selectbox('Select any Feature',options = ['Avg. Session Length','Time on App','Time on Website','Length of Membership'])
if selected_feature == 'Avg. Session Length':
    st.image('/content/drive/MyDrive/E_Commerce_Sales/avg_session_length.png')
    st.write('Boxplot indicates there are few outliers in this feature.')
    st.write("We can see the bell shape curve in the histogram plot.i.e Average Session Length follows normal distribution.")
    st.write("Average Session Length is positively correlated with Yearly Spent Amount.")
elif selected_feature == 'Time on App':
    st.image('/content/drive/MyDrive/E_Commerce_Sales/time_on_app.png')
    st.write('Boxplot indicates there are few outliers in this feature.')
    st.write("There is some skewness in this feature.")
    st.write("Time on App is positively correlated with Yearly Spent Amount.")
elif selected_feature == 'Time on Website':
    st.image('/content/drive/MyDrive/E_Commerce_Sales/time_on_website.png')
    st.write('Boxplot indicates there are few outliers in this feature.')
    st.write("We can see the bell shape curve in the histogram plot.i.e Time on Website follows normal distribution.")
    st.write("Time on Website is weakly correlated with Yearly Spent Amount.")
else:
    st.image('/content/drive/MyDrive/E_Commerce_Sales/length_of_membership.png')
    st.write('Boxplot indicates there are few outliers in this feature.')
    st.write("We can see the bell shape curve in the histogram plot.i.e Length of Membership follows normal distribution.")
    st.write("Length of Membership has strong positive correlation with Yearly Spent Amount.")

