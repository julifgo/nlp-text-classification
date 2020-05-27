from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer

# from sklearn.pipeline import Pipeline, make_pipeline

# from sklearn.metrics import classification_report

# import es_core_news_sm
# nlp = es_core_news_sm.load()

# from nltk.stem.snowball import SnowballStemmer
# stemmer = SnowballStemmer("spanish")
import sys
import os
sys.path.append(os.path.abspath('../'))
import functions as utils
from functions import transform_html, lower_cases, stemme, Word2vecTransformer, LemmatizeTransformer,StopwordsTransformer

import numpy as np
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
# %load_ext autoreload
# %autoreload 2


def htmlCleanerPipeStep():
    HtmlCleaner = FunctionTransformer(transform_html)
    clean_pipeline = ColumnTransformer([
        ("clean_title", HtmlCleaner, [0]),
        ("clean_description", HtmlCleaner, [1])
    ])
    return clean_pipeline

def lowerCasesPipeStep():
    LowerCases = FunctionTransformer(lower_cases)
    lower_pipeline = ColumnTransformer([
        ("lower_title", LowerCases, [0]),
        ("lower_description", LowerCases, [1]),
    ])
    return lower_pipeline

def stopWordsPipeStep(stopwords_path):
    stopper_pipeline = ColumnTransformer([
        ("stopper_title", StopwordsTransformer(path=stopwords_path), 0),
        ("stopper_description", StopwordsTransformer(path=stopwords_path), 1)
    ])
    return stopper_pipeline

def lemmatizePipeStep():
    lemmatize_pipeline = ColumnTransformer([
        ("lemmatize_title", LemmatizeTransformer(), 0),
        ("lemmatize_description", LemmatizeTransformer(), 1)
    ])
    return lemmatize_pipeline

def stemmizePipeStep():
    Stemmer = FunctionTransformer(stemme)
    stemmer_pipeline = ColumnTransformer([
        ("stemmer_title", Stemmer, 0),
        ("stemmer_description", Stemmer, 1)
    ])
    return stemmer_pipeline

def word2vecPipeStep():
    word2vec_pipeline = ColumnTransformer([
        ("word2vec_title", Word2vecTransformer(), 0),
        ("word2vec_description", Word2vecTransformer(), 1),
    ])
    return word2vec_pipeline

def tfIdfVectorizerPipeStep(params):
    tfidf_pipeline = ColumnTransformer([
        ("tfidf_title", TfidfVectorizer(**params), 0),
        ("tfidf_description", TfidfVectorizer(**params), 1)
    ])
    return tfidf_pipeline