import numpy as np
import pandas as pd
import requests
import sys



#parte 6 Automatizacion 
def descargar_datos(url):
    response = requests.get(url)
    name_file = 'datos_procesados.csv'
    with open(name_file, 'w', encoding='utf-8') as archivo:
        archivo.write(response.text)
    return pd.read_csv(name_file)

def categorizar_en_grupos(df): 
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels)
    return df


def main():
    url = sys.argv[1]  # Obtenemos la url desde los argumentos de la terminal
    df = descargar_datos(url)
    df_1 = categorizar_en_grupos(df)
    df_1.to_csv('datos_procesados_2.csv', index=False)

if __name__ == "__main__":
    main()



# python parte6.py https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv