import pandas as pd
import pytest
from src.preprocess import make_cleaner  


def test_clean():
    clean = make_cleaner()
    out = clean("Dogs ARE barking!!!")
    assert out == ["dog", "bark"]
