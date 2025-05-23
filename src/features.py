import pandas as pd

def add_features(data):
    data['rooms_per_house']= data['households']/data['total_rooms']
    data['people_per_house']= data['households']/data['population']

    # One-Hot Encode ocean_proximity
    data = pd.get_dummies(data, columns=['ocean_proximity'])
    return data