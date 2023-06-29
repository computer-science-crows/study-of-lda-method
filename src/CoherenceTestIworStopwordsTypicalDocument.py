from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from gensim.models import CoherenceModel
from gensim.models import LdaModel
import nltk
import os
import json
from .CoherenceTestIwor import read
from .CoherenceTestIworStopwords import parse

def document_topic(file_name,number_topics, texts):

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

# nb=10
# lines = read()
# texts = parse(lines)
# lda('dataset_1/typical_documents',nb,texts)





