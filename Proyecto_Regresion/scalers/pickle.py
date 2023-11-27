import pickle
from dataanalysis import *
from sklearn.preprocessing import StandardScaler 

# Asumimos que 'sc' es el objeto scaler
sc = StandardScaler().fit(X_train)  
scaler_file_path = 'scalers/standard_scaler.pickle' 

# Guardar el scaler en un archivo pickle
with open(scaler_file_path, 'wb') as scaler_file:
    pickle.dump(sc, scaler_file)
