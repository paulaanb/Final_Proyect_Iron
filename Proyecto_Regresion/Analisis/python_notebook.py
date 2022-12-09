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
print('Cantidad de filas: ', regression.shape[0]) 


#VALORES UNICOS
#Columna 'bedrooms'
regression['bedrooms'].unique()


#Columna 'bathrooms'
regression['bathrooms'].unique()

#Columna 'floors'
regression['floors'].unique()


#Columna 'condition'
regression['condition'].unique()

#Columna 'grade'
regression['grade'].unique()


#Ordenamos los datos en orden decreciente por el precio de la casa. 
regression.sort_values(by='price', ascending=False).head(10)['id']
 #Mostramos los 10 ids de las casas mas caras

#Precio promedio de las casas
regression['price'].mean()

#Utilizamos la funcion 'groupby' 
#Agrupamos los datos por la columna 'bedrooms' y calculamos el promedio de la columna 'price'
regression.groupby('bedrooms')['price'].mean()

#Agrupamos los datos por la columna 'bedrooms' y calculamos el promedio de lacolumna 'sqft_living' 
regression.groupby('bedrooms')['sqft_living'].mean()

#Precio promedio de las casas con 'waterfront'
regression[regression['waterfront']==1]['price'].mean()

#Precio promedio de las casas sin 'waterfront'
regression[regression['waterfront']==0]['price'].mean()

#Observamos si existe alguna correlacion entre las variables 'condition' y 'grade' 
regression[['condition', 'grade']].corr()


#plot to visually check if there is a positive correlation or negative correlation or no correlation between both variables
sns.regplot(x='condition', y='grade', data=regression)

#Observamos en la grafica que entre ambas variables ('condition' y 'grade') existe una correlación
# positiva, es decir, a mayor condición del inmueble, mayor será su calificación.
# Esto es lógico, ya que un inmueble en buenas condiciones tendrá una mejor calificación que uno en malas condiciones.


#CASAS POR CONDICIONES

#Cantidad de casas por condicion
regression['condition'].value_counts()

#Cantidad de casas por baños
regression['bathrooms'].value_counts()

#Cantidad de casas por pisos
regression['floors'].value_counts()

#Cantidad de casas por calificacion
regression['grade'].value_counts()


#Cantidad de casas por precio
regression['price'].value_counts()

#Un cliente nos pide que encontremos una casa con las siguientes categorias:

    #- 3 o 4 habitaciones
    #- Más de 3 baños
    #- 1 planta
    #- Que no tenga vistas al lago
    #- Tiene que tener por lo menos un 3 de condición
    #- La calificacion tiene que ser al menos de un 5
    #- El precio tiene que ser menos de 300000

#Creamos una variable que contenga los datos de las casas que cumplen con las condiciones
regression[((_regression['bedrooms']==3) | (regression['bedrooms']==4)) & (regression['bathrooms']>3) & (regression['floors']==1) & (regression['waterfront']==0) & (regression['condition']>=3) & (regression['grade']>=5) & (regression['price']<300000)]

#No hay ninguna casa que cumpla con las condicones que nos pide el cliente, por lo que no podemos recomendarle ninguna casa.

#Mostramos las casas que su precio es el doble de la media
regression[regression['price']>(regression['price'].mean()*2)]

#Observamos cual es la diferencia entre el precio medio de las casas con 3 habitaciones y las casas con 4 habitaciones
regression[regression['bedrooms']==4]['price'].mean() - regression[regression['bedrooms']==3]['price'].mean()

#Mostramos los distintos codigos postales
regression['zipcode'].unique()

#Mostramos las casas que han sido renovadas
regression[house_price_regression['yr_renovated']>0] 

#Mostramos los detalles de la 11º casa mas cara de nuestro dataset
regression.sort_values(by='price', ascending=False).head(11).iloc[10] 

