import streamlit as st
import joblib
import numpy as np
import datetime as dt

# Load the model from the .pkl file
model = joblib.load('bigmart_model.pkl')

# Function to make sales predictions
def make_sales_prediction():
    st.header("Big Mart Sales Prediction using Machine Learning")

    # Input fields
    item_mrp = st.number_input("Item MRP", value=0.0)
    outlet_identifier = st.selectbox("Outlet Identifier", ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'])
    outlet_size = st.selectbox("Outlet Size", ['High', 'Medium', 'Small'])
    outlet_type = st.selectbox("Outlet Type", ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])
    outlet_establishment_year = st.number_input("Outlet Establishment Year", value=2000)

    # Map outlet identifier, size, and type to numerical values
    outlet_identifier_mapping = {'OUT010': 0, 'OUT013': 1, 'OUT017': 2, 'OUT018': 3, 'OUT019': 4, 'OUT027': 5, 'OUT035': 6, 'OUT045': 7, 'OUT046': 8, 'OUT049': 9}
    outlet_size_mapping = {'High': 0, 'Medium': 1, 'Small': 2}
    outlet_type_mapping = {'Grocery Store': 0, 'Supermarket Type1': 1, 'Supermarket Type2': 2, 'Supermarket Type3': 3}

    outlet_identifier_encoded = outlet_identifier_mapping.get(outlet_identifier, 0)
    outlet_size_encoded = outlet_size_mapping.get(outlet_size, 1)
    outlet_type_encoded = outlet_type_mapping.get(outlet_type, 1)

    # Calculate the outlet age
    current_year = dt.datetime.today().year
    outlet_age = current_year - outlet_establishment_year

    # Debugging: Print input values
    st.write(f"Item MRP: {item_mrp}")
    st.write(f"Outlet Identifier Encoded: {outlet_identifier_encoded}")
    st.write(f"Outlet Size Encoded: {outlet_size_encoded}")
    st.write(f"Outlet Type Encoded: {outlet_type_encoded}")
    st.write(f"Outlet Age: {outlet_age}")

    # Predict sales using the loaded model
    model_input = np.array([[item_mrp, outlet_identifier_encoded, outlet_size_encoded, outlet_type_encoded, outlet_age]])

    try:
        prediction = model.predict(model_input)[0]
        st.subheader("Sales Prediction")
        st.write(f"Predicted Sales Amount: {prediction:.2f}")
    except Exception as e:
        st.subheader("Error")
        st.write(f"An error occurred while making the prediction: {str(e)}")

# Create the Streamlit app
if __name__ == '__main__':
    make_sales_prediction()
