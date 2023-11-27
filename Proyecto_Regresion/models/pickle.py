import pickle
from sklearn.linear_model import LinearRegression  

linear_model = LinearRegression()
linear_model.fit(X_train, y_train) 

model_file_path = 'models/linear_regression_model.pickle' 

# Guardar el modelo en un archivo pickle
with open(model_file_path, 'wb') as model_file:
    pickle.dump(linear_model, model_file)
