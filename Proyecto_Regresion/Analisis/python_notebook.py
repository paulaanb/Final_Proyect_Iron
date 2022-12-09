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
house_price_regression.drop('date', axis=1, inplace=True)
house_price_regression.head(10)

#Mostramos la cantidad de filas 
print('Cantidad de filas: ', house_price_regression.shape[0]) 


#VALORES UNICOS
#Columna 'bedrooms'
house_price_regression['bedrooms'].unique()


#Columna 'bathrooms'
house_price_regression['bathrooms'].unique()
