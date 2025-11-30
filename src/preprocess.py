import re
import nltk
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class ProcessData:
    def __init__(self, data_path: str):
        self.data_path = data_path
    
    def load_data(self):
        data = pd.read_parquet(self.data_path)

        topic_labels = {
            0: "Society & Culture",
            1: "Science & Mathematics",
            2: "Health",
            3: "Education & Reference",
            4: "Computers & Internet",
            5: "Sports",
            6: "Business & Finance",
            7: "Entertainment & Music",
            8: "Family & Relationships",
            9: "Politics & Government"
        }
        
        data["topic_name"] = data["topic"].map(topic_labels)

        return data
    
    def clean_text(self):
        stop_words = set(stopwords.words("english"))
        lemmatizer = WordNetLemmatizer()


        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)

        tokens = word_tokenize(text)

        tokens = [
            lemmatizer.lemmatize(t, pos="v") 
            for t in tokens
            if t not in stop_words
        ]
        return tokens
    
    def preprocess_data(self, data_path):
        data = self.load_data(data_path)

        data["clean_question_title"] = data["question_title"].apply( lambda text: " ".join(self.clean_text(text)))
        data["clean_question_content"] = data["question_content"].apply(lambda text: " ".join(self.clean_text(text)))
        data["clean_best_answer"] = data["best_answer"].apply(lambda text: " ".join(self.clean_text(text)))

        return data

