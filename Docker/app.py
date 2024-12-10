from flask import Flask, jsonify
import numpy as np
import pandas as pd
import requests
import tensorflow as tf  # type: ignore
from sklearn.preprocessing import MinMaxScaler
import time

app = Flask(__name__)

# Configuración de Prometheus para obtener métricas
prometheus_url = 'http://prometheus-service:9090/api/v1/query_range'

# Función para obtener las métricas de Prometheus
def get_metrics():
    query = 'rate(node_cpu_seconds_total{mode="user"}[5m])'
    params = {
        'query': query,
        'start': time.time() - 3600,  # Última hora de datos
        'end': time.time(),
        'step': '15s'
    }
    response = requests.get(prometheus_url, params=params)
    data = response.json()['data']['result']

    # Crear una lista para almacenar solo los valores
    values = []

    # Iterar sobre los resultados para procesar cada métrica
    for metric in data:
        for value in metric['values']:  # 'values' contiene múltiples [timestamp, value]
            metric_value = float(value[1])  # Convertimos el valor a float
            values.append(metric_value)

    # Convertir la lista a un DataFrame
    df = pd.DataFrame(values, columns=['value'])

    # Imprimir el DataFrame para verificar que se esté creando correctamente
    print(df.head())

    return df

# Preprocesar las métricas
def preprocess_data(df):
    # Aseguramos que no haya valores nulos
    df = df.fillna(0)
    return df

# Función para realizar la predicción usando el modelo LSTM entrenado
def predict(cpu_usage_data):
    # Normalización de los datos
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(cpu_usage_data.values.reshape(-1, 1))

    # Preparar los datos para el modelo
    time_step = 60  # 60 minutos de secuencia
    X, _ = create_dataset(scaled_data, time_step)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Cargar el modelo preentrenado
    model = tf.keras.models.load_model('predictive_model.h5')

    # Realizar la predicción
    prediction = model.predict(X)
    prediction = scaler.inverse_transform(prediction)
    return prediction[-1]

# Función para crear el dataset para el modelo LSTM
def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

# Ruta principal que ahora hace la predicción
@app.route('/')
def home():
    df = get_metrics()  # Obtener las métricas de Prometheus
    preprocessed_data = preprocess_data(df)  # Preprocesar las métricas
    prediction = predict(preprocessed_data['value'])  # Realizar la predicción
    return jsonify({"predicted_cpu_usage": prediction.tolist()})  # Retornar el resultado como JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






