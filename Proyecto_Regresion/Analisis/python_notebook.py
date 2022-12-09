import pandas as pd
import seaborn as sns
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
import statsmodels.api as sm
import pylab as plt

#Cargamos los datos
regression=pd.read_csv("regression_data.csv", sep= ";")
regression.head()

#Eliminamos la columna 'date' ya que no la utilizaremos en el analisis
regression.drop('date', axis=1, inplace=True)
regression.head(10)

#Mostramos la cantidad de filas 
print('Cantidad de filas: ', house_price_regression.shape[0]) 


#VALORES UNICOS
#Columna 'bedrooms'
house_price_regression['bedrooms'].unique()


#Columna 'bathrooms'
house_price_regression['bathrooms'].unique()

#Columna 'floors'
house_price_regression['floors'].unique()


#Columna 'condition'
house_price_regression['condition'].unique()

#Columna 'grade'
house_price_regression['grade'].unique()


#Ordenamos los datos en orden decreciente por el precio de la casa. 
house_price_regression.sort_values(by='price', ascending=False).head(10)['id']
 #Mostramos los 10 ids de las casas mas caras

#Precio promedio de las casas
house_price_regression['price'].mean()

#Utilizamos la funcion 'groupby' 
#Agrupamos los datos por la columna 'bedrooms' y calculamos el promedio de la columna 'price'
house_price_regression.groupby('bedrooms')['price'].mean()

#Agrupamos los datos por la columna 'bedrooms' y calculamos el promedio de lacolumna 'sqft_living' 
house_price_regression.groupby('bedrooms')['sqft_living'].mean()

#Precio promedio de las casas con 'waterfront'
house_price_regression[house_price_regression['waterfront']==1]['price'].mean()

#Precio promedio de las casas sin 'waterfront'
house_price_regression[house_price_regression['waterfront']==0]['price'].mean()

#Observamos si existe alguna correlacion entre las variables 'condition' y 'grade' 
house_price_regression[['condition', 'grade']].corr()


#plot to visually check if there is a positive correlation or negative correlation or no correlation between both variables
sns.regplot(x='condition', y='grade', data=house_price_regression)

#Observamos en la grafica que entre ambas variables ('condition' y 'grade') existe una correlación
# positiva, es decir, a mayor condición del inmueble, mayor será su calificación.
# Esto es lógico, ya que un inmueble en buenas condiciones tendrá una mejor calificación que uno en malas condiciones.


#CASAS POR CONDICIONES

#Cantidad de casas por condicion
house_price_regression['condition'].value_counts()

#Cantidad de casas por baños
house_price_regression['bathrooms'].value_counts()

#Cantidad de casas por pisos
house_price_regression['floors'].value_counts()

