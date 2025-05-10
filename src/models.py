from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_random_forest(X_train,y_train, params): 
    model=RandomForestRegressor(**params)
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    predictions= model.predict(X_test)
    mse=mean_squared_error(y_test,predictions)
    return mse