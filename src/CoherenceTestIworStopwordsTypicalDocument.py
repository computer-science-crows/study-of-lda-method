from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from gensim.models import CoherenceModel
from gensim.models import LdaModel
import nltk
import os
import json

# Given an object named 'texts' (a list of tokenized texts, ie a list of lists of tokens)
# from gensim.test.utils import common_texts as texts

# Create a corpus from a list of lists of tokens

nltk.download('stopwords')

def read():
    
    file = open(os.getcwd() + '/src/TokenVieuxM.txt', "r")
    lines = file.readlines()
    file.close()

    return lines

# print(stopwords.words())
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
    # End : Potential ill-characters cleaning
    # print(lt)
        ltc=[word for word in lt if not word in stopwords.words()]
       #print("C", ltc)
        texts.append(ltc)

    return texts

def lda(file_name,number_topics, texts):
    id2word = Dictionary(texts)
    corpus = [id2word.doc2bow(text) for text in texts]
   
# Train the lda model on the corpus.
    lda = LdaModel(corpus, num_topics=number_topics)
    typical_docs = lda.get_document_topics(corpus)
    docs_topics = {}
    for i,topic in enumerate(list(typical_docs)):
        print(f"Topic {topic[0][0]}: {topic[0][1]}")
        docs_topics.update({i:[str(topic[0][0]), str(topic[0][1])]})        

    with open(os.getcwd() + f'/tests/{file_name}/typical_docs.json', 'w') as file:
        json.dump(docs_topics, file)

nb=10
lines = read()
texts = parse(lines)
lda('dataset_1/typical_documents',nb,texts)





