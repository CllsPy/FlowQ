from src.train import nltk_word_tokenizer


def test_nltk_tokenizer():
    text = "nlp tokenizer"
    assert nltk_word_tokenizer(text) == ['nlp', 'tokenizer']
