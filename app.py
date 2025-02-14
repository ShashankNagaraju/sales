import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("sales.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Sales Prediction App")
st.write("Enter the advertising budget for TV, Radio, and Newspaper to predict sales.")

# Input fields
tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, step=1.0, format="%.2f")
radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, step=1.0, format="%.2f")
newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, step=1.0, format="%.2f")

# Prediction button
if st.button("Predict Sales"):
    # Convert input into array
    input_data = np.array([[tv, radio, newspaper]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"Predicted Sales: {prediction[0]:.2f} units")

# Run this using: streamlit run app.py
