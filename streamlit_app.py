import streamlit as st
import joblib
import pandas as pd
import json

st.title("Pitoniso de animales")
st.write("Este programa adivina el animal en base a lo siguiente:")
st.image("img/mascotas.jpg", use_container_width=True)

# Carga el modelo entrenado y las asignaciones para el color de ojos y el largo del pelo
model = joblib.load("model/pets_model.joblib")
with open("model/category_mapping.json", "r") as f:
    category_mapping = json.load(f)

# Extrae los valores categóricos de las asignaciones
eye_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

# Pide los datos de la mascota
weight = st.slider("Peso (Kg)", 0, 100, 50)
height = st.slider("Altura (cm)", 0, 100, 50)
eye_color = st.selectbox("Color de ojos", ["Azul", "Verde", "Marrón", "Grises"])
fur_length = st.selectbox("Largo del pelo", ["Corto", "Medio", "Largo"])

# Mapea la selección de color de ojos y largo del pelo al español
eye_color_mapping = {"Azul": "blue", "Verde": "green", "Marrón": "brown", "Grises": "gray"}
fur_length_mapping = {"Corto": "short", "Medio": "medium", "Largo": "long"}

selected_eye_color = eye_color_mapping[eye_color]
selected_fur_length = fur_length_mapping[fur_length]

# Genera las columnas binarias para eye_color y fur_length
#eye_color_binary = [int(color == selected_eye_color) for color in eye_color_values]
eye_color_binary = [(color == selected_eye_color) for color in eye_color_values]
fur_length_binary = [(length == selected_fur_length) for length in fur_length_values]

# Crea un DataFrame con los datos de la mascota
input_data = [weight, height] + eye_color_binary + fur_length_binary
columns = ["weight_kg", "height_cm"] + [f"eye_color_{color}" for color in eye_color_values] + [f"fur_length_{length}" for length in fur_length_values]
input_df = pd.DataFrame([input_data], columns=columns)

# Realiza la predicción

if st.button("Adivinar"):
    prediction = model.predict(input_df)[0]
    prediction_map = {"cat": "gato", "dog": "perro", "rabbit": "Conejo"}
    st.success(f"La mascota es un {prediction_map[prediction]}", icon="✅")
    st.balloons()