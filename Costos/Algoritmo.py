import pandas as pd

# Simulación: Costo por vCPU y RAM 
cost_per_vcpu = 0.05  # Por hora
cost_per_gb_ram = 0.01  # Por GB por hora

# Métricas de uso (Ejemplo)
current_usage = {
    "vcpu": 4,  # Número de vCPUs
    "ram_gb": 16,  # GB de RAM
    "hours": 24  # Horas de uso
}

# Configuraciones disponibles 
options = [
    {"vcpu": 2, "ram_gb": 8, "name": "config_1"},
    {"vcpu": 4, "ram_gb": 16, "name": "config_2"},
    {"vcpu": 6, "ram_gb": 32, "name": "config_3"},
]

# Función para calcular el costo
def calculate_cost(vcpu, ram_gb, hours):
    return (vcpu * cost_per_vcpu + ram_gb * cost_per_gb_ram) * hours

# Evaluar opciones
results = []
for option in options:
    cost = calculate_cost(option["vcpu"], option["ram_gb"], current_usage["hours"])
    results.append({"name": option["name"], "cost": cost})

# Mostrar opciones optimizadas
df = pd.DataFrame(results)
print("Configuraciones optimizadas:")
print(df.sort_values(by="cost"))
