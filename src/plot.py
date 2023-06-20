import matplotlib.pyplot as plt
import numpy as np
import json
import os


# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, round(y[i],4), ha = 'center')

def plot_bar(labels, values, x_label, y_label, title, name):
    
    # setting figure size by using figure() function
    plt.figure(figsize = (10,5))
     
    # making the bar chart on the data
    plt.bar(labels, values)
     
    # calling the function to add value labels
    addlabels(labels, values)
     
    # giving title to the plot
    plt.title(title)
    
    # giving X and Y labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
     
    plt.savefig(os.getcwd() + f'/doc/images/plots/{name}.png')

def read(file):
    # Abrir el archivo JSON
    with open(os.getcwd() + f'/tests/test_{file}.json') as file:
        # Cargar el contenido del archivo JSON en un objeto de Python
        data = json.load(file)

    # Acceder a los datos del archivo JSON
    return data

def plot_all(number_tests):

    for i in range(1, number_tests+1):
        data = read(i)
        for j in range(len(data.keys())-2):  
            labels = list(data[str(j)].keys()) 
            values = list(map(float, data[str(j)].values()))
            plot_bar(labels, values, 'words', 'probability', f'Test {i} - Topic {j}', f'test_{i}_topic_{j}')

plot_all(1)