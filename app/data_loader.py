import pandas as pd

def load_data():
    df = pd.read_csv("data/telco.csv")
    return df