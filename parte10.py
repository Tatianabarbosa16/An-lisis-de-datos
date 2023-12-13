# Importamos las bibliotecas necesarias
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


df = pd.read_csv('datos_procesados_2.csv')


X = df.drop(['DEATH_EVENT', 'age', 'categoria_edad'], axis=1)


y = df['age']


model = LinearRegression()

#
model.fit(X, y)


y_pred = model.predict(X)

comparison = pd.DataFrame({'Real': y, 'Predicho': y_pred})
print(comparison)


mse = mean_squared_error(y, y_pred)
print(f'El error cuadrático medio es {mse}')