import pandas as pd
from src.features import add_features

def test_add_features_creates_expected_columns():
    df = pd.DataFrame({
        'households': [400, 200],
        'total_rooms': [100, 800],
        'population': [300, 600],
        'ocean_proximity':['NEAR BAY','INLAND']
    })

    
    df_with_features = add_features(df)

    
    assert 'rooms_per_house' in df_with_features.columns
    assert 'people_per_house' in df_with_features.columns
    assert any(col.startswith("ocean_proximity_") for col in df_with_features.columns)
    
    assert df_with_features.loc[0, 'rooms_per_house'] == 400 / 100
    assert df_with_features.loc[0, 'people_per_house'] == 400 / 300
