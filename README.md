# Prototipo Optimización de la Gestión de Recursos en la Nube para Grandes Empresas
Representar la propuesta de solución de nuestro paper en la asignatura Arquitecturas Empresariales.

![image](https://github.com/user-attachments/assets/bbd05c8a-1e1e-439b-9597-4c8224a3a408)

![image](https://github.com/user-attachments/assets/409aea16-f5ed-4ebd-8d5e-c01382a76174)

## Empezando
Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba.

## prerrequisitos
* Git - Control de versiones.
* python - Lenguaje de programación.
* Docker - tecnología de organización en contenedores que posibilita la creación y el uso de los contenedores de Linux.


# Funcionamiento
1. Costos
Algoritmo.py: Lógica para calcular costos relacionados con el uso de recursos en la nube e infraestructura de Kubernetes.
2. Docker
app.py: Archivo principal de la aplicación que define la lógica de las operaciones del proyecto.
Dockerfile: Archivo de configuración para construir las imagenes Docker que ejecutan la aplicación (Prometheus y Grafana).
requirements.txt: Lista de dependencias necesarias para la aplicación Python.
deployment.yaml y service.yaml: Archivos de configuración de Kubernetes para el despliegue.
3. Carpeta Escalamiento
hpa.yaml: Configuración para el escalamiento horizontal (Horizontal Pod Autoscaler). 
vpa.yaml: Configuración para el escalamiento vertical (Vertical Pod Autoscaler). 
4. Carpeta Grafana
Archivos relacionados (grafana-deployment.yaml, grafana-service.yaml, etc.):
Se usan para desplegar Grafana en el clúster de Kubernetes.
Grafana se utiliza para visualizar métricas obtenidas de Prometheus.
5. Carpeta Prometheus
Contiene configuraciones para desplegar Prometheus y sus componentes asociados:
prometheus-deployment.yaml: Configuración para el despliegue del servidor de Prometheus.
kube-state-metrics y kubernetes-cadvisor: Recursos que recopilan métricas del clúster de Kubernetes y de los contenedores respectivamente.
node-exporter.yaml: Configura un exportador para recopilar métricas de los nodos del clúster.
prometheus-config.yaml: Archivo de configuración para Prometheus.
6. Carpeta Seguridad
role-pod-reader.yaml y rolebinding-pod-reader.yaml:
Configuran permisos de seguridad (Roles y RoleBindings) para que ciertos componentes puedan leer información de los pods en el clúster.


# Arquitectura y sus componentes

1. Entrada: Kubernetes Cluster
El proyecto se despliega en un clúster de Kubernetes, el cual actúa como la base para ejecutar los componentes principales.
Incluye los nodos del clúster, donde se despliegan:
* Pods de aplicaciones.
* Pods de monitoreo (Prometheus, Grafana).
* Recursos de seguridad y escalamiento.
2. Monitoreo: Prometheus
Componente Principal:
* Prometheus recolecta métricas del clúster, los contenedores y los nodos.
Fuentes de Métricas:
* Kube-State-Metrics: Proporciona métricas de alto nivel sobre los objetos de Kubernetes.
* cAdvisor: Proporciona métricas de uso de recursos de los contenedores.
* Node Exporter: Recolecta métricas a nivel de los nodos físicos o virtuales.
Configuración:
* Los targets desde los cuales Prometheus recolecta métricas están definidos en prometheus-config.yaml.
3. Visualización: Grafana
Grafana se conecta a Prometheus como su fuente de datos principal.
Muestra métricas clave en paneles personalizados, como:
* Uso de CPU y memoria de los pods.
* Número de réplicas ajustadas por HPA/VPA.
* Estado de los nodos del clúster.
* Grafana utiliza almacenamiento persistente configurado mediante grafana-pvc.yaml para guardar dashboards y configuraciones personalizadas.
4. Escalamiento Automático
Horizontal Pod Autoscaler (HPA):
* Ajusta dinámicamente la cantidad de réplicas de los pods según el uso de recursos u otras métricas personalizadas.
* Configurado mediante el archivo hpa.yaml.
Vertical Pod Autoscaler (VPA):
* Optimiza los recursos solicitados y los límites de los contenedores.
* Configurado mediante el archivo vpa.yaml.
* Ambos trabajan con las métricas proporcionadas por Prometheus.
5. Análisis de Costos
Lógica en Algoritmo.py:
* Recopila datos de métricas desde Prometheus.
Calcula costos asociados al uso de recursos:
* Instancias EC2.
* Recursos de Kubernetes (CPU, memoria, almacenamiento, etc.).
* La aplicación principal (app.py) podría exponer un endpoint o generar reportes basados en este análisis.
6. Seguridad
Los permisos de lectura de los pods y métricas son configurados mediante:
* role-pod-reader.yaml: Define roles específicos.
* rolebinding-pod-reader.yaml: Vincula los roles a los servicios o usuarios adecuados.
7. Docker y Despliegue
Los componentes principales son empaquetados en contenedores Docker utilizando el Dockerfile.
Estos contenedores se despliegan en el clúster utilizando:
* deployment.yaml: Define cómo desplegar la aplicación.
* service.yaml: Expone el servicio, permitiendo que sea accesible dentro o fuera del clúster.


## Flujo de funcionamiento

1. Recopilación de métricas:

Prometheus recolecta métricas de los pods, nodos y otros recursos del clúster mediante kube-state-metrics, cadvisor, y otros exportadores.
Estas métricas podrían incluir uso de CPU, memoria, redes, etc.

2. Visualización:

Las métricas recopiladas por Prometheus se visualizan en Grafana mediante dashboards configurados.

3. Escalamiento Automático:

Kubernetes ajusta los recursos (réplicas de pods, límites de CPU/memoria) basándose en las métricas proporcionadas por Prometheus, según las configuraciones de HPA y VPA.

4. Análisis de costos:

Algoritmo.py podría utilizar estas métricas para estimar los costos asociados con el uso de recursos.

5. Implementación y administración:

Los archivos en la carpeta Docker permiten empaquetar y desplegar la aplicación como un contenedor.
Los archivos YAML bajo Escalamiento, Grafana, y Prometheus orquestan el despliegue de los servicios en Kubernetes.

# Video del funcionamiento

[Link](https://www.youtube.com/watch?v=_5zuBGIaiIo&ab_channel=DiegoCastellanos)

## Versiones 
Python 3.12.5

Visual Studio Code: 1.95.1

## Autores
Diego Fernando Castellanos Amaya - [Diegoc04](https://github.com/Diegoc04)

Daniel Santiago Torres Acosta - [RulosS290](https://github.com/RulosS290)

## Agradecimientos
* Al profesor Daniel Benavides por impartir esta clase y tener la pasión de enseñar.
