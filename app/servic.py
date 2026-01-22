import pandas as pd
df =pd.read_csv("data/weapons_list.csv")


def categorization_by_impact_distance(num:int|float):
    if num < 21 :
        return "low"
    elif num < 101 :
        return "medium"
    elif num < 301:
        return "high"
    else:
        return "extreme"
    
def create_risk_level_colum(df:pd.DataFrame):
    df["risk_level"] = df["range_km"].apply(categorization_by_impact_distance)
    return df


def filling_missing_data(df:pd.DataFrame):
    df = df.fillna("Unknown")
    return df




def processing_data(df:pd.DataFrame):
    df = create_risk_level_colum(df)
    df = filling_missing_data(df)
    return df
