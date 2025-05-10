from src.data import load_data, clean_data
import pandas as pd 

def test_load_and_clean(tmp_path):
    csv= tmp_path/"sample.csv"
    df= pd.DataFrame({'total_bedrooms':[1,None],"median_house_value":[100,200]})
    df.to_csv(csv, index=False)


    data =load_data(str(csv))
    cleaned= clean_data(data)
    assert cleaned['total_bedrooms'].isnull().sum()==0
    assert "median_house_value" in cleaned.columns