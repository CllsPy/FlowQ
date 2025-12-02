import pandas as pd
import pytest
from src.preprocess import ProcessData  

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

def test_load(create_sample_data):
    process_data = ProcessData(create_sample_data)
    data = process_data.load_data()

    assert isinstance(data, pd.DataFrame)
    assert not data.empty