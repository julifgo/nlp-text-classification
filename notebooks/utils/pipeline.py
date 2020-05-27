
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
import numpy as np

stemmer = SnowballStemmer("spanish")

def stemme(df):
    return pd.Series(df).apply(lambda s: " ".join([stemmer.stem(w) for w in s.split(" ")])).to_frame()

# HtmlCleaner
REGEX_HTML = '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'
REGEX_STYLE = '<style>(.*?)<\/style>'
REGEX_MUTIBLANK = '\s\s+'
REGEX_SPECIAL = '[!,¡,*,\[\],¿,?,:,(,),#,%]'

def transform_html(df):
    return df.apply(
        lambda s: s.str.replace(REGEX_STYLE, '' , regex=True)
        .replace(REGEX_HTML, ' ' , regex=True)
        .replace(REGEX_MUTIBLANK, ' ' , regex=True)
        .replace(REGEX_SPECIAL, '' , regex=True)
        .str.strip()
        .fillna('')
        .astype('str')
    )


def lower_cases(arr): #we receive an np.array here   
    # return np.char.lower(arr.astype('str'))
    return np.char.lower(arr.astype(str))

