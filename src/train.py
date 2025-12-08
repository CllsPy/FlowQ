import pandas as pd


def load_data(path):
    df = pd.read_parquet(path)
    return df