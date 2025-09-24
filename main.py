# Assignment # 04 - Temperature Converter using Streamlit
# Author: Mohsin
# Description: Converts temperature between Celsius, Kelvin, and Fahrenheit.

import streamlit as st
from tomlkit.container import ends_with_whitespace

# --- Custom CSS for consistent colors ---
st.markdown(
    """
    <style>
    /* Heading color */
    h1 {
        color: #2E86C1; /* Blue */
        text-align: center;
    }

    /* Instruction text */
    .instruction {
        color: black;
        font-size: 18px;
        font-weight: bold;
    }

    /* Button styling */
    div.stButton > button {
        background-color:black;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        height: 45px;
        width: 220px;
    }

    div.stButton > button:hover {
        background-color: black;
        color: white;
    }

    /* Success box */
    .stSuccess {
        background-color: black !important;
        color: white !important;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Step 1: Heading ---
st.markdown("<h1>Welcome to! Temperature Converter</h1>", unsafe_allow_html=True)

# --- Step 2: Instruction message ---
st.markdown("<p class='instruction'>Select Temperature of conversion:</p>", unsafe_allow_html=True)

# --- Step 3: Radio buttons ---
conversion_type = st.radio(
    "Choose the unit you want to convert TO:",
    ("Kelvin", "Fahrenheit", "Celsius")
)

# --- Step 4: Formula dictionary ---
formulas = {
    "Kelvin": "K = °C + 273.15",
    "Fahrenheit": "°F = (°C × 9/5) + 32",
    "Celsius": "°C = K - 273.15"
}

# Show formula only after user selects
if conversion_type:
    st.write(f"Formula for {conversion_type}: **{formulas[conversion_type]}**")

# --- Step 5: Input field depends on choice ---
input_value = None
input_unit = ""

if conversion_type == "Kelvin":
    input_value = st.number_input("Enter value of °C:", format="%.2f", step=1.0)
    input_unit = "Celsius"

elif conversion_type == "Fahrenheit":
    input_value = st.number_input("Enter value of °C:", format="%.2f", step=1.0)
    input_unit = "Celsius"

elif conversion_type == "Celsius":
    input_value = st.number_input("Enter value of °K:", format="%.2f", step=1.0)
    input_unit = "Kelvin"

# --- Step 6: Convert button ---
if input_value is not None and input_value != 0.0:
    convert_btn = st.button("Convert Temperature")

    if convert_btn:
        if conversion_type == "Kelvin":
            result = input_value + 273.15
            st.success(f"T = {result:.2f} °K ...............Successfully Converted")


        elif conversion_type == "Fahrenheit":
            result = (input_value * 9/5) + 32
            st.success(f"T = {result:.2f} °F ................Successfully Converted")


        elif conversion_type == "Celsius":
            result = input_value - 273.15
            st.success(f"T = {result:.2f} °C ................Successfully Converted")
