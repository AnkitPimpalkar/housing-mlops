from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_linear_regression(X_train, y_train):
    model=LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train,y_train)
    model=RandomForestRegressor()
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    predictions= model.predict(X_test)
    mse=mean_squared_error(X_test,predictions)
    return mse