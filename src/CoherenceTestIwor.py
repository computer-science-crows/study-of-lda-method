from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from gensim.models import CoherenceModel
from gensim.models import LdaModel
import nltk
import os
import json


# Given an object named 'texts' (a list of tokenized texts, ie a list of lists of tokens)
# from gensim.test.utils import common_texts as texts


def read():
    
    file = open(os.getcwd() + '/src/TokenVieuxM.txt', "r")
    lines = file.readlines()
    file.close()

    return lines


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
    
        texts.append(lt)

    return texts




def lda(file_name,number_topics, texts, number_test):
    id2word = Dictionary(texts)
    corpus = [id2word.doc2bow(text) for text in texts]

    # Train the lda model on the corpus.
    lda = LdaModel(corpus, num_topics=number_topics)
    
    test = {}
    
    # Print topic descrition
    for i in range(0, number_topics):
        new_topic = {}
        value = lda.get_topic_terms(i)
        for j in value:
            new_topic.update({id2word[j[0]]:str(j[1])})
        test.update({i:new_topic.copy()})  
        
    # Compute Perplexity
    # a measure of how good the model is (lower the better).
    perplexity_lda = lda.log_perplexity(corpus)
    test.update({'perplexity':perplexity_lda})

    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(
        model=lda, texts=texts, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    
    test.update({'coherence':coherence_lda})   
    
    # save test
    with open(os.getcwd() + f'/tests/{file_name}/test_{number_test}.json', 'w') as file:
        json.dump(test, file)

# nb = 10
# i = 50
# while i > 0:
#     lines = read()
#     texts = parse(lines)
#     lda('dataset_1/stopwords',nb,texts,i)
#     i-=1
