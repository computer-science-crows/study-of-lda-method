import matplotlib.pyplot as plt
import numpy as np
import json
import os


# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], round(y[i],4),ha='center',  va='bottom')

def plot_bar(labels, values, x_label, y_label, title, color, file):
    
    # setting figure size by using figure() function
    plt.figure(figsize = (10,5))
     
    # making the bar chart on the data
    plt.bar(labels, values, color=color)
     
    # calling the function to add value labels
    #addlabels(labels, values)
     
    # giving title to the plot
    plt.title(title)
    
    # giving X and Y labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
     
    plt.savefig(os.getcwd() + f'/doc/images/{file}')

def plot_several_bars(data, x_label, y_label, title, name):
    
    f, axs = plt.subplots(len(data), sharey=True)
    print(f'ax {axs}')

    for i in range(len(axs)):
        print(f"data[i] {data[i]}")
        labels = list(data[i].keys())
        print(f"labels {labels}")
        values = [round(elem,4) for elem in list(map(float, data[i].values()))]
        print(f"values {values}")
        axs[i].bar(labels,values)

    f.suptitle(title)
    plt.savefig(os.getcwd() + f'/doc/images/plots/{name}.png')




def read(file_name):
    # Abrir el archivo JSON
    with open(os.getcwd() + f'/tests/{file_name}') as file:
        # Cargar el contenido del archivo JSON en un objeto de Python
        data = json.load(file)

    # Acceder a los datos del archivo JSON
    return data

def read_topic(file_name, topic):
        
    read_topics = []

    # Obtener la lista de archivos en la carpeta
    folder = [file for file in os.listdir(os.getcwd() + f'/tests/') if file.endswith('.json')]

    # Cargar y leer cada archivo .json
    for file in folder:
        print(file)
        path = os.path.join(os.getcwd() + f'/tests/', file)
        with open(path, 'r') as f:
            content = json.load(f)
            print(f"conten {content[str(topic)]}")
            read_topics.append(content[str(topic)])            

   
    return read_topics
            
def read_coherence_perplexity(file_name):

    coherence = []
    perplexity = []

    # Obtener la lista de archivos en la carpeta
    folder = [file for file in os.listdir(os.getcwd() + f'/tests/{file_name}') if file.endswith('.json')]

    # Cargar y leer cada archivo .json
    for file in folder:
        print(file)
        path = os.path.join(os.getcwd() + f'/tests/{file_name}', file)
        with open(path, 'r') as f:
            content = json.load(f)
            coherence.append(content['coherence'])
            perplexity.append(content['perplexity'])            

   
    return coherence, perplexity



def plot_all(number_topics):

    for i in range(number_topics):
        data = read_topic(i)
        print(data)
        plot_several_bars(data, 'words', 'probability', f'Topic {i}', f'topic{i}')


def plot_test(file_name, test, color):

    data = read(file_name)    
    for j in range(len(data.keys())-2):  
        labels = list(data[str(j)].keys()) 
        values = list(map(float, data[str(j)].values()))
        plot_bar(labels, values, 'words', 'probability', f"Topic {j}",color, f'plots/test_{test}_no_stopwords/topic_{j}.png')


def plot_coherence_perplexity(file_name):

    coherence, perplexity = read_coherence_perplexity(file_name)
    print(coherence)
    print(perplexity)
    labels = [i for i in range(5, len(coherence)+5)]
    print(labels)

    plot_bar(labels, coherence, 'number of topics', 'coherence', 'Coherence of Tests No Stopwords and Different Number of Topics', 'firebrick', 'coherence_no_stopwords_diff_n_topics.png')

    plot_bar(labels, perplexity, 'number of topics', 'perplexity', 'Perplexity of Tests No Stopwords and Different Number of Topics', 'cadetblue', 'perplexity_no_stopwords_diff_n_topics.png')
        
        


plot_coherence_perplexity('no_stopwords_diff_n_topics/')

#plot_test('no_stopwords/test_8.json', 8, 'steelblue')

#plot_all(5,10)
# data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
# names = list(data.keys())
# values = list(data.values())

# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Categorical Plotting')



# plt.savefig(os.getcwd() + f'/doc/images/plots/test.png')