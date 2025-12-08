import pandas as pd
import pytest

from src.train import load_data

def test_loader(create_sample_data):
    df = load_data(create_sample_data)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty