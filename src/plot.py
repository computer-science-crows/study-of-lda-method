import matplotlib.pyplot as plt
import numpy as np
import json
import os


def plot_bar(labels, values, x_label, y_label, title, color, file):
    # setting figure size by using figure() function
    plt.figure(figsize=(15, 12))

    # making the bar chart on the data
    plt.bar(labels, values, color=color)

    # add value labels
    # for i in range(len(labels)):
    #     plt.text(i, values[i], round(values[i],4),ha='center',  va='bottom')
    plt.xticks(range(len(labels)), labels, rotation='vertical')
    # giving title to the plot
    plt.title(title)

    # giving X and Y labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.savefig(os.getcwd() + f'/doc/images/{file}')

def plot_line(labels, values, x_label, y_label, title, color, file):
    
    # Plotear el gráfico con líneas y puntos
    plt.plot(labels, values, '-o', color=color)

    # Personalizar el gráfico
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    

    plt.savefig(os.getcwd() + f'/doc/images/{file}')
    

def read(file_name):
    # Abrir el archivo JSON
    with open(os.getcwd() + f'/tests/{file_name}') as file:
        # Cargar el contenido del archivo JSON en un objeto de Python
        data = json.load(file)

    # Acceder a los datos del archivo JSON
    return data


def plot_test(file_name, test, color):
    data = read(file_name)
    for j in range(len(data.keys())-2):
        labels = list(data[str(j)].keys())
        values = list(map(float, data[str(j)].values()))
        plot_bar(labels, values, 'words', 'probability',
                 f"Topic {j}", color, f'plots/test_{test}/topic_{j}.png')


def read_coherence_perplexity(file_name):
    coherence = []
    perplexity = []

    # Obtener la lista de archivos en la carpeta
    folder = [file for file in os.listdir(
        os.getcwd() + f'/tests/{file_name}') if file.endswith('.json')]

    # Cargar y leer cada archivo .json
    for file in folder:
        path = os.path.join(os.getcwd() + f'/tests/{file_name}', file)
        with open(path, 'r') as f:
            content = json.load(f)
            coherence.append(content['coherence'])
            perplexity.append(content['perplexity'])

    return coherence, perplexity


def plot_coherence_perplexity(file_name):
    coherence, perplexity = read_coherence_perplexity(file_name)
    labels = [i for i in range(5, len(coherence)+ 5)]
    
    plot_line(labels, coherence, 'number of topics', 'coherence',
             'Coherence vs Number of Topics (No Stopwords)', 'orchid', 'coherence_no_stopwords_diff_n_topics.png')
    plt.clf()

    plot_line(labels, perplexity, 'number of topics', 'perplexity',
             'Perplexity vs Number of Topics (No Stopwords)', 'lightgreen', 'perplexity_no_stopwords_diff_n_topics.png')


plot_coherence_perplexity('dataset_1/no_stopwords_diff_n_topics/')

#plot_test('dataset_1/stopwords/test_5.json', 5, 'lightskyblue')

# coherence, perplexity = read_coherence_perplexity('dataset_1/stopwords/')
# print(f"D1 Stopwords Coherence {sum(coherence)/len(coherence)}")
# print(f"D1 Stopwords Perplexity {sum(perplexity)/len(perplexity)}")
# coherence, perplexity = read_coherence_perplexity('dataset_1/no_stopwords/')
# print(f"D1 No Stopwords Coherence {sum(coherence)/len(coherence)}")
# print(f"D1 No Stopwords Perplexity {sum(perplexity)/len(perplexity)}")
# coherence, perplexity = read_coherence_perplexity('dataset_2/no_stopwords/')
# print(f"D2 No Stopwords Coherence {sum(coherence)/len(coherence)}")
# print(f"D2 No Stopwords Perplexity {sum(perplexity)/len(perplexity)}")