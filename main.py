import streamlit as st
import joblib
import requests
from io import BytesIO

# Load the model from the GitHub URL
model_url = "https://github.com/harshcshah/Big-mart-sales-prediction/raw/main/bigmart_model.pkl"
response = requests.get(model_url)
model = joblib.load(BytesIO(response.content))

# Function to make sales predictions
def make_sales_prediction(item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age):
    # Create a data input for prediction
    model_input = [item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age]
    
    # Make a prediction
    prediction = model.predict([model_input])[0]

    return prediction

# Streamlit UI elements
st.title("Big Mart Sales Prediction using Machine Learning")

item_mrp = st.number_input("Item MRP", min_value=0.00)
outlet_identifier = st.text_input("Outlet Identifier")
outlet_size = st.selectbox("Outlet Size", ["High", "Medium", "Small"])
outlet_type = st.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
outlet_age = st.number_input("Outlet Establishment Year")

if st.button("Predict"):
    prediction = make_sales_prediction(item_mrp, outlet_identifier, outlet_size, outlet_type, outlet_age)
    st.write(f"Predicted Sales: {prediction:.2f}")
