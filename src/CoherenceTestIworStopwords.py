from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from gensim.models import CoherenceModel
from gensim.models import LdaModel
import nltk
import os
import json
from .CoherenceTestIwor import read, lda

nltk.download('stopwords')

def parse(lines):
    texts = []

    for line in lines:
        line = line.strip()
        lt = line.split(",")

        # Potential ill-character cleaning
        for i in range(len(lt)):
            lt[i] = lt[i].replace('[', '')
            lt[i] = lt[i].replace(']', '')
            lt[i] = lt[i].replace('"', '')
            lt[i] = lt[i].replace('\n', '')
            lt[i] = lt[i].replace(' ', '')
    
        # Remove stopwords
        ltc=[word for word in lt if not word in stopwords.words()]
        
        texts.append(ltc)

    return texts


# for i in range(5,21):
#     lines = read()
#     texts = parse(lines)
#     lda('dataset_1/no_stopwords_diff_n_topics',i,texts,i)
    
