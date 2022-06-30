
from util import read_data 
from init.init_solution1 import load_init1
from init.init_solution2 import load_init2
from util.read_data import load_list_target
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CHOICE
from util.fitness import get_fitness_and_point, sum_fitness
from util.mutate import choice_list_mutate, mutate_chromosomes
from util.crossover import choice_list_crossover, crossover_chromosomes

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
    '''
    Lua chon cac ca the khoe mang sang quan thee tiep theo
    '''
    list_index_choice = []
    while len(list_index_choice) < SIZE_CHOICE:
        index_choice = random.random()
        for i in range (0, len(probability)):
            if probability[i][0] <= index_choice and probability[i][1] >= index_choice:
                list_index_choice.append(i)
                break

    return list_index_choice

def find_best_individual(population):
    max_fitness = 0
    for individual in population:
        fitness_i = individual.get_fitness()
        if fitness_i> max_fitness:
            max_fitness = fitness_i
            best_individual = individual
    return best_individual

def next_step(population):
    new_population = []

    #Thang co fitness tot nhat duoc ton tai 
    best_individual = find_best_individual(population)
    new_population.append(best_individual)

    #lay cac thong so cho vong quay roulette
    sum_f = sum_fitness(population)
    probability = selection_probability(population, sum_f)

    #chon cac ca the khoe manh ton tai
    list_index_choice = selection_chromosomes(probability)
    for i in list_index_choice:
        new_population.append(population[i])

    #chon ca the lai ghep
    list_index_couple_choice = choice_list_crossover(population)
    for couple_choice in list_index_couple_choice:
        new_individual1, new_individual2 = crossover_chromosomes(couple_choice, population)
        new_population.append(new_individual1)
        new_population.append(new_individual2)

    # chon ca the dot bien
    list_index_choice = choice_list_mutate(population)
    for index in list_index_choice:
        new_individual = mutate_chromosomes(population[index])
        new_population.append(new_individual)

    return new_population 


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
    count = 0
    index = 0
    sum_f_pre = 0
    while count < 50:
        if sum_f_pre == sum_f: 
            count += 1
        else:
            sum_f = 0
        
        sum_f_pre = sum_f

        population = next_step(population)
        
        sum_f = sum_fitness(population)

        best_individual = find_best_individual(population)
        print("ca the tot nhat sau {} vong lap: {}".format(index,best_individual.get_fitness()))

    
