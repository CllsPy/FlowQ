import pandas as pd
import pytest
from src.preprocess import load_data  

@pytest.fixture
def create_sample_data():
    df = pd.DataFrame(
        {
            "topic":[0, 5, 9]
        }
    )

    path = "tests/data/tiny_data.parquet"
    df.to_parquet(path)
    return path

def test_load_data(create_sample_data):
    df = load_data(create_sample_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty