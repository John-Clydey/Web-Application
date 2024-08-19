import streamlit as st
import back_end as BE

# Upper Part of my program
st.title("Clydey's Converter App")
st.write("Go down deep enough into anything and you will find mathematics.—Dean Schlicter")

# this is for my theme
st.markdown(
    """
    <style>
    .stApp{
        background-color : #F8EAC8;

    }
    </style>
    """,
    unsafe_allow_html=True

)
# a widget being added
toggle_button = st.toggle("Switch Conversion")

if toggle_button:
    st.title("BINARY TO DECIMAL CONVERTER🧮")
    binary_input = st.text_input("Enter binary number: ", key="binary_number")

    if not binary_input.isdigit() or set(binary_input) - {'0', '1'}:
        st.error("Please enter a valid binary number (0s and 1s only).")
    else:
        convert_button = st.button("Convert")
        st.session_state["convert_button"] = convert_button
        if convert_button:
            decimal_num = BE.binary_to_decimal(binary_input)
            st.session_state["decimal_number"] = decimal_num
            st.text_input("Binary number equivalent to Decimal", value=str(decimal_num))
            print(st.session_state)

else:
    st.title("DECIMAL TO BINARY CONVERTER🧮")
    decimal_input = st.text_input("Enter a decimal integer number: ", key="decimal_number")

    if not decimal_input.isdigit():
        st.error("Please enter a valid integer number.")
    else:
        convert_button = st.button("Convert")
        st.session_state["convert_button"] = convert_button
        if convert_button:
            binary_num = BE.decToBin(int(decimal_input))
            st.session_state["binary_number"] = binary_num
            st.text_input("Binary number equivalent to Decimal", value=str(binary_num))
            print(st.session_state)
