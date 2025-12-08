import re

import nltk

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')


import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# --- I/O ---
def load_data(path):
    df = pd.read_parquet(path)
    return df

# --- Clean Data ---
def make_cleaner():
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    def clean(text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)

        tokens = word_tokenize(text)
        return [
            lemmatizer.lemmatize(t, pos="v")
            for t in tokens
            if t not in stop_words
        ]

    return clean 

# --- Preprocessing  ---
def preprocess(df, clean_fn):
    df = df.copy()
    df["clean_question_title"] = df["question_title"].apply(lambda t: " ".join(clean_fn(t)))
    df["clean_question_content"] = df["question_content"].apply(lambda t: " ".join(clean_fn(t)))
    df["clean_best_answer"] = df["best_answer"].apply(lambda t: " ".join(clean_fn(t)))
    return df

# --- Save Data ---
def transform_and_save_data(path, save_path):
    df = load_data(path)
    clean = make_cleaner()
    df = preprocess(df, clean)
    df.to_parquet(save_path, index=False)
    return df


if __name__ == "__main__":
    df = transform_and_save_data(path="data/data_combined.parquet", save_path="data/data_preprocessed.parquet")
    print(df)
