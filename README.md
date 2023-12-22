# Ana-lisis-de-datos 
# Parte 1: Carga y Análisis Inicial de Datos
Cargar el dataframe de `fallas_cardiacas`.
Seleccionar la columna de `edad` y convertirla a un array de NumPy.
Calcular y mostrar el promedio de las edades.

# Parte 2: Preprocesamiento de Datos
 Convertir la estructura `Dataset` en un DataFrame de Pandas usando `pd.DataFrame`.
 Separar el dataframe en dos: uno con las filas de personas que fallecieron (`is_dead=1`) y otro con el resto.
 Calcular y mostrar los promedios de las edades de cada dataset.

# Parte 3: Creación y Verificación de Columnas
Verificar que los tipos de datos son correctos en cada columna.
Crear las columnas 'sex' y 'smoking' en el DataFrame.
Verificar si las columnas "sex" y "smoking" existen en el DataFrame.
Calcular y mostrar la cantidad de hombres fumadores vs mujeres fumadoras.

# Parte 4: Descarga de Datos
Realizar un GET request para descargar los datos necesarios.
Escribir la respuesta como un archivo de texto plano con extensión csv.
Agrupar el código en una función reutilizable que reciba como argumento la url.

# Parte 5: Limpieza de Datos
 Verificar que no existan valores faltantes.
Verificar que no existan filas repetidas.
Verificar si existen valores atípicos y eliminarlos.
Crear una columna que categorice por edades.
Guardar el resultado como csv.

# Parte 6: Automatización de Procesos
Descargar el archivo necesario usando los métodos aprendidos en clase (`with open as file`).
Categorizar los datos por edad.
Automatizar los pasos anteriores, permitiendo el uso de una url como argumento para ejecutar nuestro código.

# Parte 7: Visualización de Datos  Histogramas
Utilizar las librerías de visualización y manejo de datos previamente aprendidas.
Crear un histograma con la distribución de las edades de las personas.
Crear otro histograma para visualizar los datos de hombres y mujeres que padecen: Anemia, Diabetes, Fuman y Han muerto.

# Parte 8: Visualización de Datos  Gráficos de Torta
Utilizar los datos de la parte anterior para crear gráficos de torta, permitiendo ver una mejor distribución con porcentajes.
Personalizar los gráficos utilizando las funcionalidades de las librerías.

# Parte 9: Visualización de Datos  Gráfico 3D
Utilizar un gráfico 3D para visualizar de manera más detallada la distribución de las personas que han muerto.
Aplicar la técnica de reducción de dimensionalidad para visualizar aproximadamente la estructura de nuestros datos.

# Parte 10: Regresión Lineal
Cargar los datos procesados anteriormente.
Eliminar las columnas `DEATH_EVENT` y `age` del dataframe para que sea la matriz X.
Ajustar una regresión lineal sobre el resto de columnas y usar la columna `age` como vector y.
Predecir las edades y comparar con las edades reales.
Calcular el error cuadrático medio.

# Parte 11: Árbol de Decisión
Cargar los datos procesados nuevamente.
Verificar si la columna 'smoking' existe en el DataFrame.
Eliminar la columna `categoria_edad` del dataframe para que sea la matriz X.
Ajustar una regresión lineal sobre el resto de columnas y usar la columna `smoking` como vector y.
Graficar la distribución de clases.
Realizar la división del dataset en conjunto de entrenamiento y test.
Ajustar el árbol de decisión.
Predecir las clases y comparar con las clases reales.
Calcular el accuracy.

# Parte 12: Random Forest
Ajustar un random forest.
Predecir nuevamente las clases y comparar con las clases reales.
Calcular el accuracy.
Calcular el F1-Score.
Calcular la matriz de confusión.
