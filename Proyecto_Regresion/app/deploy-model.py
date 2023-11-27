import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Cargar los datos
regression = pd.read_csv("regression_data.csv", sep=";")

# Eliminar la columna 'date'
regression.drop('date', axis=1, inplace=True)

# Separar los datos en características (X) y variable objetivo (y)
X = regression.drop('price', axis=1)
y = regression.price

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=22)

# Escalar los datos
scaler = StandardScaler().fit(X_train)
X_train_sc = scaler.transform(X_train)
X_test_sc = scaler.transform(X_test)

# Entrenar el modelo
linear_model = LinearRegression()
linear_model.fit(X_train_sc, y_train)

# Guardar el modelo en un archivo pickle
with open('models/linear_regression_model.pickle', 'wb') as model_file:
    pickle.dump(linear_model, model_file)

# Guardar el scaler en un archivo pickle
with open('scalers/standard_scaler.pickle', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Configurar la aplicación Streamlit
st.title("House Price Prediction App")

# Agregar controles de entrada para las características del modelo
bedrooms = st.slider("Bedrooms", min_value=1, max_value=5, value=3)
bathrooms = st.slider("Bathrooms", min_value=1, max_value=5, value=2)
sqft_living = st.slider("Square Footage of Living Area", min_value=500, max_value=5000, value=2000)

# Realizar la predicción cuando se hace clic en el botón
if st.button("Predict Price"):
    # Crear un diccionario con las características ingresadas
    input_features = {
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
    }

    # Cargar el modelo y el scaler desde los archivos pickle
    with open('models/linear_regression_model.pickle', 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    with open('scalers/standard_scaler.pickle', 'rb') as scaler_file:
        loaded_scaler = pickle.load(scaler_file)

    # Escalar las características de entrada
    input_data = pd.DataFrame([input_features])
    input_data_sc = loaded_scaler.transform(input_data)

    # Realizar la predicción
    prediction = loaded_model.predict(input_data_sc)
    st.success(f"The predicted price of the house is ${prediction[0]:,.2f}")
