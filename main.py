import streamlit as st
import numpy as np
import datetime as dt

# Function to make sales prediction
def make_sales_prediction():
    p1 = st.text_input("Item_MRP", type="float", value=0.0)
    p5 = st.text_input("Outlet_Establishment_Year", type="int", value=2000)

    outlet_identifier = st.selectbox("Outlet Identifier", ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'])
    outlet_size = st.selectbox("Outlet Size", ['High', 'Medium', 'Small'])
    outlet_type = st.selectbox("Outlet Type", ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])

    p2 = options.index(outlet_identifier)
    p3 = options0.index(outlet_size)
    p4 = options1.index(outlet_type)

    if st.button('Predict'):
        try:
            p1 = float(p1)
            p5 = int(p5)
            model_input = np.array([[p1, p2, p3, p4, p5]])
            result = model.predict(model_input)[0]
            st.write("Sales amount:", result)
        except (ValueError, IndexError):
            st.error("Please enter valid values for prediction.")

# Your code for loading the model and making predictions
# Make sure your 'model' variable is defined here.

# Your model loading code
model = joblib.load('bigmart_model')

current_year = dt.datetime.today().year
options = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049']
options0 = ['High', 'Medium', 'Small']
options1 = ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3']

st.title("Big Mart Sales Prediction using Machine Learning")
make_sales_prediction()
