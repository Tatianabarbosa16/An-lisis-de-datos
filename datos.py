import numpy as np
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")


data = dataset["train"]


ages = np.array(data['age'])


average_age = np.mean(ages)

print(f"El promedio de edad de las personas participantes en el estudio es {average_age}")