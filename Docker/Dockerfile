# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor (incluyendo requirements.txt)
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Expone el puerto que usará Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

