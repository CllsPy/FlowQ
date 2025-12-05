import pandas as pd
import pytest
from src.preprocess import load_data  


def test_load_data(create_sample_data):
    df = load_data(create_sample_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty