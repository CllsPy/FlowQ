import pandas as pd
import pytest
import os
from src.preprocess import transform_and_save_data


def test_transform_and_save(create_sample_data):
    save_path = "tests/data/new_data.parquet"
    
    df = transform_and_save_data(create_sample_data, save_path)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

