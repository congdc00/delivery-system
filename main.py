
from util import read_data 
from init.init_solution1 import load_init1
from init.init_solution2 import load_init2
from util.read_data import load_list_target
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CROSSOVER
from util.fitness import get_fitness_and_point, sum_fitness
import random

def selection_probability(population, sum_fitness):
    min_q = 0 # xác xuất tích lũy
    max_q = 0
    probability = []
    for i in range(0, len(population)):
        p = population[i].get_fitness()/sum_fitness
        max_q += p
        probability.append([min_q, max_q])
        min_q = max_q

    return probability

def selection_chromosomes(probability):
    list_index_choice = []
    while len(list_index_choice) < SIZE_CROSSOVER:
        index_choice = random.random()
        for i in range (0, len(probability)):
            if probability[i][0] <= index_choice and probability[i][1] >= index_choice:
                list_index_choice.append(i)
                break

    return list_index_choice

if __name__ == "__main__":

    list_target = load_list_target(ROOT_PATH_DATA)
    

    population = []

    list_trip_drone, list_trip_truck, list_target_result = load_init1()
    individual = Individual(0, list_trip_drone, list_trip_truck, list_target_result)

    point, fitness = get_fitness_and_point(list_target, list_target_result)
    individual.update_fitness(fitness)
    individual.update_point(point)

    population.append(individual)

    list_trip_drone, list_trip_truck, list_target_result = load_init2()
    individual = Individual(0, list_trip_drone, list_trip_truck, list_target_result)
    point, fitness  = get_fitness_and_point(list_target, list_target_result)
    individual.update_fitness(fitness)
    individual.update_point(point)

    population.append(individual)

    sum_f = sum_fitness(population)
    probability = selection_probability(population, sum_f)
    index_choice = selection_chromosomes(probability)
    print(index_choice)
    