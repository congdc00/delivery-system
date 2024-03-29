import random

import sys

sys.path.append('/Users/dinhchicong/Project/delivery-system/back_end/schedule_delivery')

from calculator.fitness_and_point import sum_fitness
from util.duplicate import copy_individual

def selection_probability(population):
    sum_fitness_population, min_fitness = sum_fitness(population)
    min_q = 0 # xác xuất tích lũy
    max_q = 0
    probability = []
    for i in range(0, len(population)):
        fitness = population[i].get_fitness() + min_fitness
        p = fitness/sum_fitness_population
        max_q += p
        probability.append([min_q, max_q])
        min_q = max_q

    return probability

def selection_chromosomes(id, population):
    probability = selection_probability(population)
    
    num_random = random.random()
    for i in range (0, len(probability)):
            if probability[i][0] <= num_random and probability[i][1] >= num_random:
                new_individual = copy_individual(id, population[i])
                return new_individual
    

    
       