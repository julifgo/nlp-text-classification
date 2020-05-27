import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from tqdm.notebook import tqdm
from .spacy_mixin import SpacyMixin


class Word2vecTransformer(SpacyMixin, TransformerMixin, BaseEstimator):

    def __init__(self, pbar=None):
        pass

    def _obtain_vec(self):
        def transform_text(text):
            try:
                return SpacyMixin.nlp(text, disable=["tagger", "parser", "ner"]).vector
            except:
                print("error happend: ", text)

        return transform_text

    def fit(self, x, y=None):
        return self

    def transform(self, texts, y=None):
        """
        texts: pd.Series
        """

        self._load_nlp()
        texts_vectors = None

        if not isinstance(texts, pd.Series):
            texts = pd.Series(texts)

        texts_vectors = texts.apply(self._obtain_vec())

        return np.asmatrix(texts_vectors.explode()).reshape(-1, 50)

# transformer = Word2vecTransformer()
# print(transformer.fit(pd.Series(["Perro"])).transform(pd.Series(["Perro"])))
# pipeline = Pipeline([
#     ('union', ColumnTransformer(
#         [
#             # Pulling features from the post's subject line (first column)
#             ('subject', transformer, 0),
#             # ('subject1', transformer, 1),
#         ],
#     ))
# ])

# print(pipeline.fit_transform(pd.DataFrame([["Aloha", "pepin"], ["Aloha", "pepin"]])).shape)
