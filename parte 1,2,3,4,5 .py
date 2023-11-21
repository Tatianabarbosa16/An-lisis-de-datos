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

print(data.dtypes)

male_smokers = data[(data['is_male'] == True) & (data['is_smoker'] == True)].shape[0]
female_smokers = data[(data['is_male'] == False) & (data['is_smoker'] == True)].shape[0]
print(f"Hay {male_smokers} hombres fumadores y {female_smokers} mujeres fumadoras.")
 