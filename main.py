import streamlit as st
import joblib
import numpy as np
import datetime as dt

current_year = dt.datetime.today().year

st.title("Big Mart Sales Prediction")

# Input fields
item_mrp = st.number_input("Item MRP", min_value=0.0)
outlet_identifier = st.selectbox("Outlet Identifier", ["OUT010", "OUT013", "OUT017", "OUT018", "OUT019", "OUT027", "OUT035", "OUT045", "OUT046", "OUT049"])
outlet_size = st.selectbox("Outlet Size", ["High", "Medium", "Small"])
outlet_type = st.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
establishment_year = st.number_input("Outlet Establishment Year")

if st.button("Predict"):
    p2 =  # Map outlet_identifier to a numerical value
    p3 =  # Map outlet_size to a numerical value
    p4 =  # Map outlet_type to a numerical value
    p5 = current_year - establishment_year

    # Load the pre-trained model
    model = joblib.load('bigmart_model')
    result = model.predict(np.array([[item_mrp, p2, p3, p4, p5]]))

    # Display the prediction
    st.write(f"Predicted Sales: {result[0]}")
