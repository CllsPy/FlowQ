import pandas as pd
from nltk.tokenize import word_tokenize


def load_data(path):
    df = pd.read_parquet(path)
    return df

def nltk_word_tokenizer(text):
    text = word_tokenize(text)
    return text

def train_model():
    pass
