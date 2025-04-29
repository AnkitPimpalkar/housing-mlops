def add_features(data):
    data['rooms_per_house']= data['households']/data['total_rooms']
    data['people_per_house']= data['households']/data['population']
    return data
