# Angela Correa NC = 0037
print("Pandas")
print("+-++++-+-+-+-+-+")
import pandas as pd
print(pd.__version__) # Output: 1.5.2

print("+-++++-+-+-+-+-+")
print("Ejemplo 2 Caso Práctico en Código (Python + Pandas)")
print("+-++++-+-+-+-+-+")
import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos = {
    'distancia_km': [2.5, 4.0, 1.2, 5.8, 3.1],
    'trafico_nivel': [1, 3, 1, 3, 2],        # 1: Bajo, 2: Medio, 3: Alto
    'edad_repartidor': [22, 35, 19, 28, 40],
    'tiempo_entrega_min': [15, 32, 10, 42, 25] # Lo que queremos predecir
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("+-++++-+-+-+-+-+")
print("3. Reto de Aprendizaje Basado en Problemas (ABP)")
print("+-++++-+-+-+-+-+")

import pandas as pd

# Crear el dataset de pacientes
datos = {
    "id_paciente": [101, 102, 103, 104, 105],
    "edad": [25, 45, 36, 52, 29],
    "nivel_glucosa": [90, 160, 110, 180, 95],
    "presion_arterial": [115, 140, 120, 150, 110],
    "indice_masa_corporal": [22.5, 31.2, 27.0, 34.5, 24.0],
    "diagnostico_diabetes": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(datos)

# Mostrar el dataset completo
print("DATASET COMPLETO:")
print(df)

# Eliminar la columna que no aporta información útil
df = df.drop(columns=["id_paciente"])

# Identificar el Target (y)
y = df["diagnostico_diabetes"]

# Identificar las Features (X)
X = df.drop(columns=["diagnostico_diabetes"])

# Mostrar los resultados
print("\nFEATURES (X):")
print(X)

print("\nTARGET (y):")
print(y)

print("\nCOLUMNAS ELIMINADAS:")
print("id_paciente")

print("\nPROGRAMA EJECUTADO CORRECTAMENTE")

print("+-++++-+-+-+-+-+")
print("# Problema 14.")
import pandas as pd

datos14 = {
    'distancia_km': [5.6, 2.2, 3.0, 1.6, 4.8],
    'trafico_nivel': [3, 1, 2, 3, 2],
    'edad_repartidor': [42, 23, 33, 27, 39],
    'tiempo_entrega_min': [54, 16, 24, 18, 40]
}

df14 = pd.DataFrame(datos14)

print(df14)
print("Angela Correa NC = 0037")