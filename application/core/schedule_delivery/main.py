﻿'''
su dung Genetic Algorithm
'''
from pickletools import read_unicodestring1

from calculator.weight import sum_weight
from object.target import Target
from util import load_data 
from init.solution0 import init_solution0
from init.solution1 import init_solution1
from init.solution_random import init_solution_random
from util.load_data import load_list_target, load_list_device
from calculator.distant import set_distant
from util.show import show_info_individual, show_info_population
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CHOICE
from calculator.fitness_and_point import sum_point, sum_fitness
from GA.mutate import choice_mutate, mutate_chromosomes
from GA.crossover import choice_list_crossover, crossover_chromosomes, build_matrix_crossover_point
from GA.selection import selection_chromosomes
from GA.education import education
from util.duplicate import copy_individual
from GA.screening import choice_new_population
from util.show import show_histogram, show_map

def find_best_individual(id, population):
    max_fitness = 0
    index_max = 0
    for i in range(0,len(population)):
        fitness_i = population[i].get_fitness()
        if fitness_i > max_fitness:
            max_fitness += fitness_i
            index_max = i

    best_individual = copy_individual(id, population[index_max])

    # max_fitness = 0
    # for i in range(0,len(population)):
    #     fitness_i = population[i].get_fitness()
    #     if fitness_i > max_fitness:
    #         max_fitness = fitness_i
    #         index_max = i

    # best_individual = copy_individual(id, population[index_max])
    return best_individual


def create_param():
    #Khoi tao kho:
    depot = Target(-1, 0, 0, 0,0,0)
    
    #Khoi tao list target
    list_target = load_list_target(ROOT_PATH_DATA)

    
    depot, list_target, matrix_distance = set_distant(depot, list_target)

    # Khoi tao hang doi drone va truck
    list_device = load_list_device()

    return depot, list_device, list_target, matrix_distance

if __name__ == "__main__":


  
    depot, list_device, list_target, matrix_distance = create_param() 
    
    max_point = 0
    for target in list_target:
        _,upper_bound = target.get_bound()
        weight = target.get_weight()
        max_point += weight*upper_bound
    print("diem toi da: {}".format(max_point)) 

    list_solution_choice = [init_solution0, init_solution1] 

    # Tao init solution
    population = []
    index = -1
    for init_solution in list_solution_choice:
        index += 1
        new_list_device, new_list_target = init_solution( list_device, depot, list_target )
        new_individual = Individual(index, new_list_device, new_list_target)
        
        population.append(new_individual)
        # show_info_individual(new_individual, text="init_solution")

    for i in range (2, 100):
        index += 1
        new_list_device, new_list_target = init_solution_random( list_device, depot, list_target )
        new_individual = Individual(index, new_list_device, new_list_target)
        population.append(new_individual)
        
    
    
    fitness_log =[]
    count = 0
    max_fitness = 0
    for i in range (0, 20):
        print("\t ------------------------------vong lap thu {} -----------------------------".format(i))
        
        
        population_tmp = []
        id = 0
        
        #Chon individual tot nhat
        best_individual = find_best_individual(id, population)
        population_tmp.append(best_individual)
        
        #Chon loc
        for j in range (0,20):
            id += 1
            individual_choice = selection_chromosomes(id, population)
            population_tmp.append(individual_choice)

        #Lai ghep
        for j in range (0, 40):
            id += 2
            matrix_crossover = build_matrix_crossover_point(population)
            
            individual_adam, individual_eva = choice_list_crossover(population, matrix_crossover, rank = j)
            new_individual1, new_individual2 = crossover_chromosomes(id, individual_adam, individual_eva)

            population_tmp.append(new_individual1)
            population_tmp.append(new_individual2)

            

        #Dot bien
        for j in range (0,20):
            id += 1
            individual_choice = choice_mutate(population)
            # show_info_individual(individual_choice, text="truoc dot bien")
            new_individual = mutate_chromosomes(id, individual_choice)
            # show_info_individual(new_individual, text="sau dot bien")
            population_tmp.append(new_individual)
        
        population_tmp = education(population_tmp, matrix_distance)

        population = choice_new_population(population_tmp)
        show_info_population(population, type = "mini")

        fitness_tmp = population[0].get_fitness()
        fitness_log.append(fitness_tmp)
        if max_fitness == fitness_tmp:
            count += 1
            
        else:
            max_fitness = fitness_tmp
            count =0 
        
        if fitness_tmp == 1.0:
            break

    show_map(best_individual)

    