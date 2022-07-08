﻿'''
su dung Genetic Algorithm
'''

from object.target import Target
from util import load_data 
from init.solution0 import init_solution0
from init.solution1 import init_solution1
from util.load_data import load_list_target, load_list_device
from calculator.distant import set_distant
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CHOICE
from calculator.fitness_and_point import sum_point, sum_fitness
from GA.mutate import choice_mutate, mutate_chromosomes
from GA.crossover import choice_list_crossover, crossover_chromosomes, build_matrix_crossover_point
from GA.selection import selection_chromosomes



def find_best_individual(population):
    max_point = 0
    for i in range(0,len(population)):
        point_i = population[i].get_point()
        if point_i> max_point:
            max_point = point_i
            index_max = i

    return population[index_max]


def create_param():
    #Khoi tao kho:
    depot = Target(-1, 0, 0, 0,0,0)
    
    #Khoi tao list target
    list_target = load_list_target(ROOT_PATH_DATA)
    depot, list_target = set_distant(depot, list_target)

    # Khoi tao hang doi drone va truck
    list_drone, list_truck = load_list_device()

    return depot, list_drone, list_truck, list_target

if __name__ == "__main__":

  
    depot, list_drone, list_truck, list_target = create_param()  

    list_solution_choice = [init_solution0, init_solution1]

    # Tao init solution
    population = []
    index = -1
    for init_solution in list_solution_choice:
        index += 1
        new_list_drone, new_list_truck, new_list_target = init_solution( list_drone, list_truck,depot, list_target )
        new_individual = Individual(index, new_list_drone, new_list_truck, new_list_target)
        population.append(new_individual)

    for i in range (0, 100):
        new_population = []
        
        #Chon individual tot nhat
        best_individual = find_best_individual(population)
        new_population.append(best_individual)

        #Chon loc
        for j in range (0,2):
            individual_choice = selection_chromosomes(population)
            new_population.append(individual_choice)

        #Lai ghep
        for j in range (0, 2):
            matrix_crossover = build_matrix_crossover_point(population)
            individual_adam, individual_eva = choice_list_crossover(population, matrix_crossover, rank = 0)
            new_individual1, new_individual2 = crossover_chromosomes(individual_adam, individual_eva)
            new_population.append(new_individual1)
            new_population.append(new_individual2)

        #Dot bien
        for j in range (0,1):
            individual_choice = choice_mutate(population)
            new_individual = mutate_chromosomes(individual_choice)
            new_population.append(new_individual)

       
        population = new_population

        
        print("------------------------------vong lap thu {} -----------------------------".format(i))
        print("<lai ghep>")
        print("ca the bo: {}".format(individual_adam.get_list_target()[0].get_trip()))
        print("ca the me: {}".format(individual_eva.get_list_target()[0].get_trip()))
        print("ca the con 1: {}".format(new_individual1.get_list_target()[0].get_trip()))
        print("ca the con 2: {}".format(new_individual2.get_list_target()[0].get_trip()))
        print("<dot bien>")
        print("ca the lua chon :{}".format(individual_choice.get_list_target()[0].get_trip()))
        print("ca the do bien xong: {}".format(new_individual.get_list_target()[0].get_trip()))
        print("<info>")
        print("Best point = {}".format(best_individual.get_point()))
        print("Best fitness = {}".format(best_individual.get_fitness()))
        print("sum point: {}".format(sum_point(population)))
        print("sum fitness: {}".format(sum_fitness(population)))


   

    
