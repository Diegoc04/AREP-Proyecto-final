import requests
import pandas as pd

# Define la URL de Prometheus con la consulta directamente incluida
prometheus_url = (
    'http://localhost:32476/api/v1/query?query=rate(node_cpu_seconds_total{mode="user"}[5m])'
)

# Realiza la solicitud
response = requests.get(prometheus_url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()['data']['result']
    
    # Procesa los resultados en un DataFrame
    metrics = []
    for item in data:
        metric = item['metric']
        value = item['value']
        metrics.append({
            'cpu': metric.get('cpu', 'unknown'),
            'instance': metric.get('instance', 'unknown'),
            'job': metric.get('job', 'unknown'),
            'value': float(value[1]),  # El valor de la métrica
            'timestamp': pd.to_datetime(float(value[0]), unit='s')  # El tiempo en formato legible
        })
    
    # Crea el DataFrame
    df = pd.DataFrame(metrics)
    print(df.head())  # Muestra las primeras filas
else:
    print(f"Error en la consulta: {response.status_code} - {response.text}")

# Convertir las métricas a formato de tiempo y valores numéricos
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df['value'] = df['value'].astype(float)

# Opcionalmente, agregar más columnas para diferentes métricas (memoria, red, etc.)

# Asegúrate de que tus datos estén correctamente alineados para el entrenamiento
df = df.set_index('timestamp')
df = df.resample('1T').mean()  # Promedia los datos por minuto
df = df.fillna(0)  # Rellena valores faltantes con 0

print(df.head())

