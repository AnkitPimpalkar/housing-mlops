from src.data import load_data, clean_data
from src.features import add_features
from src.models import train_random_forest, evaluate_model
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import yaml
import datetime
import shutil
import os

os.environ["MLFLOW_TRACKING_URI"] = "file:///C:/Users/HP/ML Housing pro/mlruns"



with open('config.yaml','r')as f:
    config = yaml.safe_load(f)


def plot_feature_importance(model,features):
     importances= model.feature_importances_
     indices=pd.Series(importances,index=features).sort_values(ascending=False)

     plt.figure(figsize=(8,6))
     indices.plot(kind='bar')
     plt.title('Feature Importance')
     plt.ylabel('Importance')
     plt.tight_layout()
     plt.savefig('outputs/feature_importance.png')
     mlflow.log_artifact('outputs/feature_importance.png')


def main():
    run_name = f"{config['model']['type']}_run_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

    with mlflow.start_run(run_name=run_name):
        mlflow.set_tracking_uri("file:///C:/Users/HP/ML Housing pro/mlruns")
        mlflow.set_tag('model',config['model']['type'])
        mlflow.set_tag('developer','Ankit')
        mlflow.set_tag('stage','development')
        mlflow.set_tag('version','1.0')

        try:
            git_commit = subprocess.check_output(['git','rev-parse','HEAD']).decode('ascii').strip()
            mlflow.set_tag('git_commit',git_commit)
        except Exception as e:
            print('Git commit hash not logged', e)
        
        mlflow.log_artifact('config.yaml')
        shutil.copy('requirements.txt','requirements_logged.txt')
        mlflow.log_artifact('requirements_logged.txt')

        data=load_data(config['data']['url'])
        data=clean_data(data)
        data=add_features(data)

        target="median_house_value"
        features= [col for col in data.columns if col != target]
        X=data[features]
        y=data[target]
        X_train, X_test, y_train, y_test=train_test_split(X,y, test_size= config['split']['test_size'],random_state= config['split']['random_state'])

        mlflow.log_param("model_type",config["model"]["type"])
        mlflow.log_param("test_size",config['split']['test_size'])
        params=config['model']['params']
        for key, value in params.items():
            mlflow.log_param(key,value)

        rf= train_random_forest(X_train,y_train, params)
        rf_mse= evaluate_model(rf,X_test,y_test)

        predictions = rf.predict(X_test)
        residuals = y_test - predictions

        results_df = pd.DataFrame({
            "actual": y_test,
            "predicted": predictions,
            "residual": residuals
        })
        results_df.to_csv("outputs/predictions.csv", index=False)
        mlflow.log_artifact("outputs/predictions.csv")

        plt.figure(figsize=(8, 6))
        plt.scatter(predictions, residuals, alpha=0.5)
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel("Predicted Values")
        plt.ylabel("Residuals")
        plt.title("Residual Plot")
        plt.tight_layout()
        plt.savefig("outputs/residual_plot.png")
        mlflow.log_artifact("outputs/residual_plot.png")

        mlflow.log_metric("mse",rf_mse)
        mlflow.sklearn.log_model(rf,"model", input_example=X_train)
        plot_feature_importance(rf,features)

        print(f"Random Forest MSE: {rf_mse}")

if __name__=="__main__":
    main()