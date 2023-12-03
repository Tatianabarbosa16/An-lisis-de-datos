import numpy as np
import pandas as pd
import requests
from datasets import load_dataset
import sys


# Carga  dataset
dataset = load_dataset("mstz/heart_failure")

# Conversion de la estructura  a  un dataframe en pandas 
df = pd.DataFrame(dataset["train"])

# Separacion del dataframe  en dos  diferentes 
df_dead = df[df['is_dead'] == 1]
df_alive = df[df['is_dead'] == 0]

# Calculos dedades dat
ages = np.array(df['age'])
average_age = np.mean(ages)
average_age_dead = np.mean(df_dead['age'])
average_age_alive = np.mean(df_alive['age'])

# Resultados
print(f"El promedio de edad de las personas participantes en el estudio es {average_age}") 
print(f"Promedio de edad de las personas que perecieron  en el estudio es {average_age_dead}")
print(f"Promedio de edad de las personas que sobrevivieron en el estudio es {average_age_alive}") 

print(df.dtypes)

male_smokers = df[(df['is_male'] == True) & (df['is_smoker'] == True)].shape[0]
female_smokers = df[(df['is_male'] == False) & (df['is_smoker'] == True)].shape[0]
print(f"Hay {male_smokers} hombres fumadores y {female_smokers} mujeres fumadoras.")
 
#Parte 4 Apis
def descargar_datos(url, nombre_nuevo_archivo):
    respuesta = requests.get(url)
    with open(nombre_nuevo_archivo, 'w') as archivo:
        archivo.write(respuesta.text)
        
    descargar_datos('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv', 'datos.csv')

#Parte 5 limpieza de datos 
def procesamiento_de_datos(df):
    try:
        valores_faltantes = df.isnull().sum().sum()
        if valores_faltantes > 0:
            raise ValueError(f"El DataFrame tiene {valores_faltantes} valores faltantes.")
    except ValueError as e:
        print(e)

    try:
        filas_repetidas = df.duplicated().sum()
        if filas_repetidas > 0:
            raise ValueError(f"El DataFrame tiene {filas_repetidas} filas duplicadas.")
    except ValueError as e:
        print(e)

    Q1 = df['age'].quantile(0.25)
    Q3 = df['age'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df['age'] < (Q1 - 1.5 * IQR)) | (df['age'] > (Q3 + 1.5 * IQR)))]

    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels)



    df.to_csv('datos_procesados.csv', index=False)
    return df


df_limpio = procesamiento_de_datos(df)



