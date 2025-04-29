import pandas as pd
def load_data(url):
    data = pd.read_csv(url)
    return data

def clean_data(data):
    data = data.dropna(subset=["total_bedrooms"])
    return data
