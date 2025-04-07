import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder


# Load the trained model
model = tf.keras.models.load_model('model.h5')

### Load the encoders and scaler
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('ohe.pkl', 'rb') as file:
    ohe = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

### Streamlit app
st.title("Customer Churn Prediction")

### User input
geography = st.selectbox("Geography", ohe.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance', 0.0, 250000.0, step=100.0)
credit_score = st.number_input('Credit Score', 0, 850, step=1)
estimated_salary = st.number_input('Estimated Salary', 0.0, 200000.0, step=100.0)
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
is_early_exit = st.selectbox('Is Early Exit', [0, 1])

### Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
})

### One-hot encode the geography column
geography_encoded = ohe.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geography_encoded, columns=ohe.get_feature_names_out(['Geography']))

### Concatenate the encoded geography with the input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

### Scale the input data
input_data_scaled = scaler.transform(input_data)

### Predict the churn probability
prediction = model.predict(input_data_scaled)   
prediction = prediction[0][0]
probability = prediction * 100

st.write(f"Churn Probability: {probability:.2f}%")
st.write("This customer is likely to churn." if probability > 50 else "This customer is not likely to churn.")