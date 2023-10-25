import streamlit as st
import pandas as pd
import joblib
import requests
from io import BytesIO

# Function to load the model from GitHub
def load_model_from_github():
    url = 'https://github.com/harshcshah/Big-mart-sales-prediction/raw/main/bigmart_model.pkl'
    response = requests.get(url)
    model = joblib.load(BytesIO(response.content))
    return model

# Load the pre-trained model
model = load_model_from_github()

# Function to make sales predictions
def make_sales_prediction(item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age):
    model_input = [item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age]
    prediction = model.predict([model_input])[0]
    return prediction

# App title and description
st.title('Big Mart Sales Prediction using Machine Learning')
st.write('Enter the following details to predict sales:')

# Input fields
item_mrp = st.number_input('Item MRP', min_value=0.0)
outlet_identifier = st.text_input('Outlet Identifier')
outlet_size = st.text_input('Outlet Size')
outlet_type = st.text_input('Outlet Type')
outlet_age = st.number_input('Outlet Establishment Year', min_value=0)

# Predict button
if st.button('Predict'):
    prediction = make_sales_prediction(item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age)
    st.write(f'Predicted Sales: {prediction:.2f}')
