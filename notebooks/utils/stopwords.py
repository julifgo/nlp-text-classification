"""
 Read stopwords in spanish
"""

import unidecode
from nltk.corpus import stopwords

def get_stopwords(path = '../../data/other/stopwords.txt'):
    stop_arr = stopwords.words('spanish')

    with open(path) as f:
        for line in f:
            stop_arr.append(unidecode.unidecode(line.strip()))

    stop_arr = sorted(list(set(stop_arr)))

    return stop_arr
    