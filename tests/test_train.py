import pandas as pd
import pytest
from src.preprocess import ProcessData  


def test_load_data():
    test_data = pd.DataFrame({"topic": [0, 5, 9]})
    test_data.to_parquet("tests/data/tiny_data.parquet")

    process_data = ProcessData("tests/data/tiny_data.parquet")
    data = process_data.load_data()

    assert "topic_name" in data.columns
