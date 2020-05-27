import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from ..stopwords import get_stopwords
from nltk.tokenize import word_tokenize 

class StopwordsTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, path='../data/other/stopwords.txt'):
        if path is None:
            # no debería entrar por acá, pero parece que a veces lo hace
            path = '../../data/other/stopwords.txt'
        self.stopwords = get_stopwords(path)

    def fit(self, x, y=None):
        return self

    def parse(self, text):
        word_tokens = word_tokenize(text) 
        filtered_sentence = [w for w in word_tokens if not w in self.stopwords] 
        return " ".join(filtered_sentence)

    def transform(self, texts, y=None):
        """
        texts: pd.Series
        """
        if (not isinstance(texts, pd.Series)):
            texts = pd.Series(texts)
        return texts.apply(self.parse).to_frame()