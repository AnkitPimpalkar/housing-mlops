import pandas as pd
import numpy as np
from sklearn.datasets import make_regression
from src.models import train_random_forest, evaluate_model

def test_train_random_forest_returns_model():
    # Generate dummy regression data
    X, y = make_regression(n_samples=100, n_features=4, noise=0.1, random_state=42)
    X = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
    
    params = {"n_estimators": 10, "random_state": 42}
    
    model = train_random_forest(X, y, params)
    
    assert model is not None
    assert hasattr(model, "predict")
    assert model.n_estimators == 10

def test_evaluate_model_returns_float():
    X, y = make_regression(n_samples=100, n_features=4, noise=0.1, random_state=42)
    X = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
    
    model = train_random_forest(X, y, {"n_estimators": 10, "random_state": 42})
    mse = evaluate_model(model, X, y)
    
    assert isinstance(mse, float)
    assert mse >= 0
