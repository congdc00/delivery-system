from turtle import width
from config import SIZE_CROSSOVER
import random
import copy

import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual

def sum_difference(individual0, individual1):
    '''
    Ham tinh su khac biet giua hai ca the
    '''
    list_target0 = individual0.get_list_target()
    list_target1 = individual1.get_list_target()
    num_target = len(list_target0)
    sum_dif = 0
    for i in range (0, num_target):
        status_target0 = list_target0[i].get_status()
        status_target1= list_target1[i].get_status()
        sum_dif += abs(status_target0 - status_target1)
    
    return sum_dif



def build_matrix_crossover_point(population):
    matrix_crossover = []
    index_row = -1
    for individual0 in population:
        index_row += 1
        matrix_crossover.append([])
        for individual1 in population:
            crossover_point = sum_difference(individual0, individual1)
            matrix_crossover[index_row].append(crossover_point)

    return matrix_crossover

def choice_list_crossover(population, matrix_crossover, rank):

    point_crossover = 0
    index_best_choice = [0, 0]
    
    if rank == 0:
        rows = len(matrix_crossover)
        columns = len(matrix_crossover[0])
        for i in range (0, rows):
            for j in range (0, columns):
                if point_crossover < matrix_crossover[i][j]:
                    index_best_choice = [i, j]
    
    return population[index_best_choice[0]], population[index_best_choice[1]]

def crossover_chromosomes(id, individual_adam, individual_eva):

    '''
    Nên chọn 2 thằng nào có sự khác biệt nhất để lai ghép
    '''
    individual_son0 = copy.deepcopy(individual_adam)
    individual_son1 = copy.deepcopy(individual_eva)

    list_target0 = individual_son0.get_list_target()
    list_target1 = individual_son1.get_list_target()
    num_target = len(list_target0)

    for i in range (0, num_target):
        # cut trip
        target0 = list_target0[i]
        list_trip0 = target0.get_trip()
        num_trip0 = len(list_trip0)
        num_choice0 = random.randint(0,num_trip0)
        list_trip_pop_target_0 = target0.pop_trip_from(num_choice0)

        target1 = list_target1[i]
        list_trip1 = target1.get_trip()
        num_trip1 = len(list_trip1)
        num_choice1 = random.randint(0,num_trip1)
        list_trip_pop_target_1 = target1.pop_trip_from(num_choice1)

        #append trip
        for trip in list_trip_pop_target_0:
            target1.add_trip(trip)

        for trip in list_trip_pop_target_1:
            target0.add_trip(trip)

        individual_son0.update_target(target0, i)
        individual_son1.update_target(target1, i)

    new_individual0 = copy_individual(id-1, individual_son0)
    new_individual1 = copy_individual(id, individual_son1)

    return new_individual0, new_individual1
    #