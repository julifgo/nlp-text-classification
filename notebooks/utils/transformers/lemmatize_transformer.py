import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from .spacy_mixin import SpacyMixin


class LemmatizeTransformer(TransformerMixin, BaseEstimator, SpacyMixin):

    def __init__(self):
        pass

    def _obtain_lemma_doc(self, texts):
        return [ " ".join([text.lemma_ for text in doc ]) for doc in SpacyMixin.nlp.pipe(texts, disable=["tagger", "parser", "ner"])]

    def fit(self, x, y=None):
        return self

    def transform(self, texts, y=None):
        """
        texts: pd.Series
        """

        self._load_nlp()
        
        if not isinstance(texts, pd.Series):
            texts = pd.Series(texts)
        return pd.Series(self._obtain_lemma_doc(texts)).to_frame()
