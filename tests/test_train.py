import pandas as pd
import pytest
from src.train import ProcessData  


def test_load_data():
    process_data = ProcessData("data/data_combined.parquet")
    data = process_data.load_data()

    assert "topic_name" in data.columns
