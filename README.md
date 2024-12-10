# Prototipo Optimización de la Gestión de Recursos en la Nube para Grandes Empresas
Representar la propuesta de solución de nuestro paper en la asignatura Arquitecturas Empresariales.

## Empezando
Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba.

## prerrequisitos
* Git - Control de versiones.
* python - Lenguaje de programación.
* Docker - tecnología de organización en contenedores que posibilita la creación y el uso de los contenedores de Linux.

## Instalación 
Para instalar el proyecto en su maquina local realizaremos los siguientes pasos.

1. clone el proyecto con el siguiente comando: git clone https://github.com/Diegoc04/AREP-2024-2.git
2. Muevase a la carpeta Arep-2024-2 con el comando: cd Arep-2024-2/
3. muevase a la rama RAG con el comando: git checkout RAG
4. Abra el proyecto en su IDE y en el archivo "RAGserver.py" en la linea 12 modifique "API_KEY" con su llave.

## Ejecutar la aplicación

1. ejecute las celdas del archivo "langchainbasicapp.ipynb" para instalar las dependecias necesarias.

2. Ejecute el archivo "langchainserver.py", puede utilizar el siguiente comando: 'python RAGserver.py' o correrlo directamente en el IDE.

   ![image](https://github.com/user-attachments/assets/e004521e-750d-4738-8f39-2df1e3530f85)


3. Dirijase a la siguiente URL: http://localhost:8000/ask/playground

![image](https://github.com/user-attachments/assets/e6d13cf1-2f3d-4e13-a890-7b9c6713359b)


# Funcionamiento

RAG (Retrieval-Augmented Generation),  usa información de su base de datos (normalmente una base de datos vectorial que almacena representaciones de texto o "embeddings") para responder preguntas.
La información que usa para responder las preguntas se encuentra en el archivo documents.json, si hacemos uan pregunta la cual no tenga del .json no sdira que no tiene información, en caso del traductor usa el modelo de gpt-4 con acceso libre a sus librerias para poder traducir los textos del ingles a los idiomas pre-establecidos.


<p align="center">
  <img src="https://github.com/user-attachments/assets/c79ea30a-1229-4df6-8f3a-308eb9094853" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/24af3e3e-a100-4d61-a72a-585549f9d8f3" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/d0844c39-fdae-4014-85c4-f436f7ce7388" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf4efbc-5ece-4dd1-8dc2-1c8c4f4ef89c" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/422c0d67-fc82-4efc-b299-e3d85c1232b8" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1133a268-4616-4be0-a753-017aae80cbf6" alt="image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/947fa8e6-653e-43d6-a519-5f557a339580" alt="image">
</p>




# Arquitectura y sus componentes

1. FastAPI como Framework Principal de la API:
   
FastAPI es el framework principal para construir el API. Maneja la lógica de las rutas y la comunicación con el cliente.
Define los endpoints ask y translate, los cuales reciben solicitudes HTTP POST, además de servir una página HTML estática para probar la API.
Monta archivos estáticos para incluir los recursos necesarios como CSS y JavaScript en el playground.

2. Base de Datos Vectorial (VectorDatabase):
   
Este componente usa FAISS (Facebook AI Similarity Search) para realizar búsquedas vectoriales.
FAISS permite almacenar y recuperar documentos basados en similitud, con embeddings generados por el modelo de lenguaje de OpenAI.
Los documentos se almacenan como embeddings en un índice vectorial, lo que facilita la búsqueda rápida y precisa de los textos más relevantes para una pregunta.
El modelo de embeddings utilizado es OpenAIEmbeddings, que transforma cada documento y consulta en un vector numérico de 1536 dimensiones.

3. Modelo de Lenguaje (ChatOpenAI):
   
ChatOpenAI se encarga de procesar el contexto y la pregunta, generando respuestas en lenguaje natural.
Este componente recibe prompts formateados que incluyen contexto específico (documentos recuperados) y la pregunta del usuario.
Funciona también para la funcionalidad de traducción, donde toma el texto y el idioma objetivo y genera la traducción correspondiente.

Esto permite una administración ordenada de recursos y evita que se mantengan abiertos recursos de manera innecesaria.

4. Documentos JSON:
   
Los documentos iniciales se cargan desde un archivo JSON (documents.json), que contiene el contenido de texto que se usa para responder preguntas.
Estos documentos se convierten en embeddings y se cargan en la base de datos vectorial al iniciar la aplicación.

5. Interfaz de Usuario en HTML y JavaScript:
   
La aplicación incluye un playground en HTML donde los usuarios pueden realizar preguntas o traducciones directamente.
La lógica del frontend está en JavaScript, que envía las solicitudes a los endpoints /ask y /translate y actualiza el contenido en la interfaz.

6. Pruebas Unitarias con Pytest:
   
Se incluye un conjunto de pruebas unitarias que usan pytest y TestClient de FastAPI para simular solicitudes HTTP.
Se utiliza una versión simulada del modelo de lenguaje (FakeLLM) para verificar el funcionamiento de los endpoints sin depender de la API de OpenAI, lo cual facilita las pruebas en entornos controlados.

## Flujo de funcionamiento

1. Carga de Documentos: Al iniciar, los documentos se cargan en la base de datos vectorial desde un archivo JSON.
2. Consulta y Recuperación: El endpoint /ask recibe la pregunta, consulta la base de datos vectorial para obtener documentos relevantes y construye un prompt que se envía al modelo de lenguaje.
3. Traducción de Texto: El endpoint /translate recibe un texto y un idioma de destino, luego utiliza el modelo de lenguaje para generar una traducción.
4. Respuesta al Usuario: Las respuestas se devuelven en formato JSON, ya sea para preguntas o traducciones, y se presentan en la interfaz si se utiliza el playground.


# Ejecutar las pruebas 

Para ejecutar las pruebas utilice el siguiente comando: pytest test_main.py

![image](https://github.com/user-attachments/assets/4be67840-e835-4058-b419-de7cbb725002)

## Construido con
[Visual Studio Code]([https://netbeans.apache.org/front/main/download/nb22/](https://code.visualstudio.com/)) - entorno de desarrollo.

[python]([https://www.java.com/es/](https://www.python.org/)) - Lenguaje de programación.

[jupyter]([https://www.docker.com/](https://jupyter.org/)) - Documentación de codigo en vivo.

## Versiones 
Python 3.12.5

Visual Studio Code: 1.95.1

## Autores
Diego Fernando Castellanos Amaya - [Diegoc04](https://github.com/Diegoc04)

## Agradecimientos
* Al profesor Daniel Benavides por impartir esta clase y tener la pasión de enseñar.
