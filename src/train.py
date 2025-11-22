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
        
