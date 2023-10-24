import streamlit as st
import joblib
import numpy as np
import datetime as dt

current_year = dt.datetime.today().year

st.title("Big Mart Sales Prediction")

# Input fields
item_mrp = st.number_input("Item MRP", min_value=0.0)
outlet_identifier = st.selectbox("Outlet Identifier", [9.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 0.0])
outlet_size = st.selectbox("Outlet Size", [1.0, 0.0, 2.0])
outlet_type = st.selectbox("Outlet Type", [1.0, 2.0, 3.0, 0.0])
establishment_year = st.number_input("Outlet Establishment Year")

if st.button("Predict"):
    p1 = item_mrp
    p2 = outlet_identifier
    p3 = outlet_size
    p4 = outlet_type
    p5 = current_year - establishment_year

    # Load the pre-trained model using joblib
    model = joblib.load('bigmart_model.pkl')

    result = model.predict(np.array([[p1, p2, p3, p4, p5]])

    # Display the prediction
    st.write(f"Predicted Sales: {result[0]}")
    st.write(f"Sales Value is between {result[0]-714.42} and {result[0]+714.42}")
