import streamlit as st
import numpy as np
import datetime as dt
import joblib  # Ensure you have joblib installed

# Function to make sales prediction
def make_sales_prediction():
    p1 = float(st.text_input("Item_MRP"))
    p5 = current_year - int(st.text_input("Outlet_Establishment_Year"))
    
    outlet_identifier = st.selectbox("Outlet Identifier", ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'])
    outlet_size = st.selectbox("Outlet Size", ['High', 'Medium', 'Small'])
    outlet_type = st.selectbox("Outlet Type", ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])
    
    p2 = options.index(outlet_identifier)
    p3 = options0.index(outlet_size)
    p4 = options1.index(outlet_type)
    
    if st.button('Predict'):
        result = model.predict(np.array([[p1, p2, p3, p4, p5]]))
        st.write("Sales amount", result)

# Your code for loading the model and making predictions
current_year = dt.datetime.today().year
options = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049']
options0 = ['High', 'Medium', 'Small']
options1 = ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3']

# Load your model here
model = None  # Replace with the code to load your model

st.title("Big Mart Sales Prediction using Machine Learning")

make_sales_prediction()
