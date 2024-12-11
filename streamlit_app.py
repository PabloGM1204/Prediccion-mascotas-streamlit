import streamlit as st

st.title("Suma dos números")
st.write("Este programa hara que sume dos números")

num_1 = 0
num_2 = 0

num_1 = st.number_input("Dime un número")
num_2 = st.number_input("Dime otro número")

if (num_1 and num_2) != 0.0:
    st.write(f"La suma de {num_1} y {num_2} es {num_1 + num_2}")