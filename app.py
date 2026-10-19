
"""Browser-based calculator using Streamlit."""

import streamlit as st

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered",
)

st.title("🧮 Interactive Calculator")
st.write(
    "A beginner-friendly calculator and unit converter "
    "built with Python."
)

tab1, tab2, tab3 = st.tabs(
    ["Calculator", "Unit Converter", "Currency Converter"]
)

with tab1:
    st.subheader("Basic Arithmetic")

    operation = st.selectbox(
        "Choose an operation",
        ["Addition (+)", "Subtraction (-)",
         "Multiplication (*)", "Division (/)"],
    )

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("First number", value=10.0)
    with col2:
        b = st.number_input("Second number", value=5.0)

    if st.button("Calculate", key="calculate", type="primary"):
        if operation == "Addition (+)":
            result = a + b
        elif operation == "Subtraction (-)":
            result = a - b
        elif operation == "Multiplication (*)":
            result = a * b
        elif b == 0:
            st.error("Division by zero is not allowed.")
            result = None
        else:
            result = a / b

        if result is not None:
            st.success(f"Result: {result:g}")


with tab2:
    st.subheader("Unit Conversion")

    conversion = st.selectbox(
        "Choose a conversion",
        [
            "Kilometers to Miles",
            "Miles to Kilometers",
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius",
        ],
    )

    value = st.number_input("Value to convert", value=10.0)

    if st.button("Convert", key="convert", type="primary"):
        if conversion == "Kilometers to Miles":
            result = value * 0.621371
            unit = "miles"
        elif conversion == "Miles to Kilometers":
            result = value * 1.609344
            unit = "km"
        elif conversion == "Celsius to Fahrenheit":
            result = value * 9 / 5 + 32
            unit = "°F"
        else:
            result = (value - 32) * 5 / 9
            unit = "°C"

        st.success(f"Result: {result:.2f} {unit}")


with tab3:
    st.subheader("Currency Conversion")

    st.info(
        "Demo rates only: USD/INR = 85 and EUR/INR = 95. "
        "These are examples, not live exchange rates."
    )

    currency_options = {
        "USD to INR": ("USD", "INR", 85.0),
        "INR to USD": ("INR", "USD", 1 / 85.0),
        "EUR to INR": ("EUR", "INR", 95.0),
    }

    currency = st.selectbox(
        "Choose a currency pair",
        list(currency_options.keys()),
    )
    amount = st.number_input(
        "Amount to convert",
        min_value=0.0,
        value=100.0,
    )

    if st.button("Convert Currency", key="currency", type="primary"):
        source, target, rate = currency_options[currency]
        result = amount * rate
        st.success(f"{amount:.2f} {source} = {result:.2f} {target}")

st.divider()
st.caption("Built with Python and Streamlit | Internship Project")
