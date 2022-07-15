from turtle import width
from config import SIZE_CROSSOVER,NUM_DRONE
import random
import copy

import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual
from util.find import find_device_by_id
from object.individual import Individual

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
    '''
    Chọn 2 thằng nào có sự khác biệt nhất để lai ghép
    '''

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

def cut_trips(target):
    '''
    cat trip tu mot diem bat ky
    OUTPUT = 
    '''
    list_trip = target.get_trip()
    num_trip = len(list_trip)
    num_choice = random.randint(0,num_trip)
    list_cut = target.pop_trip_from(num_choice)
    return list_cut

def append_trip(trip, target):
    target.add_trip(trip)

def crossover_chromosomes(id, individual_adam, individual_eva):

    individual_son0 = copy.deepcopy(individual_adam)
    individual_son1 = copy.deepcopy(individual_eva)

    list_target0 = individual_son0.get_list_target()
    list_device0 = individual_son0.get_list_device()

    list_target1 = individual_son1.get_list_target()
    list_device1 = individual_son1.get_list_device()

    num_target = len(list_target0)

    for i in range (0, num_target):
        
        target0 = list_target0[i]
        target1 = list_target1[i]

        # cut trip
        list_cut0 = cut_trips(target0)
        list_cut1 = cut_trips(target1)

        #append trip
        for trips, target, list_device in zip([list_cut0,list_cut1],[target1, target0],[list_device0, list_device1]):
            if trips != []:
                for trip in trips:
                    append_trip(trip, target)
                    #id_device = trip[0]
                    
                    # cap nhap trip cho device
                    #device = list_device[id_device]
                    # device.change_trip(index_trip, target.get_id(), type = "id_target")


    new_individual0 = Individual(id-1, list_device0,  list_target0)
    new_individual1 = Individual(id,list_device1, list_target1)

    return new_individual0, new_individual1