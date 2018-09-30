#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due October 1st, 2018
#

import json
import csv
import numpy as np
from collections import defaultdict #honestly dont know what this is
import math
 
def histogram_times(filename):
    answer = [0] * 24
    with open(filename) as f1: #took from jupyter example
        csv_reader = csv.reader(f1)
        airplane_data = list(csv_reader)
        for time in airplane_data[1:]:
            if time[1]:
                if_time = time[1]
                try:
                    time_of_day = int(if_time.split(':')[0])
                    answer[time_of_day] += 1
                except:
                    pass #ignore all the errors
    return answer

def weigh_pokemons(filename, weight):
    pokemonNames = []
    with open(filename) as f1:
        data = json.load(f1)
        for pokemon in data["pokemon"]:
            compare = float (pokemon["weight"].split(" ")[0])
            if compare == weight:
                pokemonNames.append(pokemon ["name"])
                
                               
    return pokemonNames
    
def single_type_candy_count(filename):
    allCandy = 0;
    with open(filename) as f1:
        data = json.load(f1)
        for pokemon in data["pokemon"]:
            if len(pokemon["type"]) == 1:
                if "candy_count" in pokemon:
                    allCandy += pokemon["candy_count"]
    return allCandy

def reflections_and_projections(points):
    #pt 1
    answer = np.array(points)
    answer[1] = (answer * -1) + 2
    #pt 2
    copy = np.copy(answer)
    answer[0] = answer[1] * -1
    answer[1] = copy[0]
    #pt 3
    multiply = [[1,3], [3,9]]
    answer = np.multiply(multiply, answer) 
    answer = answer / 10 

def normalize(image):
    image2 = np.array(image)
    maxi = np.max(image)
    mini = np.min(image)
    image2 = (255 / (maxi - mini)) * (image - mini)
    return image2

def sigmoid_normalize(image, a):
    image2 = np.array(image)
    image2 = 255 * ((1 + math.exp((-a ** -1)*(image - 128)))** -1)
    return image2
    
