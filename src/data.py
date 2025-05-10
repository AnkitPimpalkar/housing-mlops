import pandas as pd

def load_data(url):
    Raw_data=pd.read_csv(url)
    data=Raw_data.copy()
    return data

def clean_data(data):
    data = data.dropna(subset=["total_bedrooms"])
    return data
