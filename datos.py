import numpy as np
import pandas as pd
from datasets import load_dataset

# Carga  dataset
dataset = load_dataset("mstz/heart_failure")

# Conversion de la estructura  a  un dataframe en pandas 
data = pd.DataFrame(dataset["train"])

# Separacion del dataframe  en dos  diferentes 
data_dead = data[data['is_dead'] == 1]
data_alive = data[data['is_dead'] == 0]

# Calculos dedades dat
ages = np.array(data['age'])
average_age = np.mean(ages)
average_age_dead = np.mean(data_dead['age'])
average_age_alive = np.mean(data_alive['age'])

# Resultados
print(f"El promedio de edad de las personas participantes en el estudio es {average_age}") 
print(f"Promedio de edad de las personas que perecieron  en el estudio es {average_age_dead}")
print(f"Promedio de edad de las personas que sobrevivieron en el estudio es {average_age_alive}") 