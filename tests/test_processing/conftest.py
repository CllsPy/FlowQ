
import pandas as pd
import pytest

@pytest.fixture
def create_sample_data():
    df = pd.DataFrame({
        "question_title":["dOGs are mad!!"],
        "question_content": ["dOGs are mad!!"],
        "best_answer":["dOGs are mad!!"]

        })
    
    tmp_path = "tests/data"
    path = tmp_path + "/tiny_data.parquet"
    df.to_parquet(path)
    return path
