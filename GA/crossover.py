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

def cut_trips(target, list_device):
    '''
    cat trip tu mot diem bat ky
    OUTPUT = 
    '''
    list_trip = target.get_trip()
    num_trip = len(list_trip)
    num_choice = random.randint(0,num_trip-1)
    list_cut, list_num = target.pop_trip_from(num_choice)

    # cap nhap lai device
    if len(list_cut) != 0:
        for trip, num in zip(list_cut,list_num):
            id_device = trip[0]
            list_device[id_device].pop_target(target.get_id(), num)

    return list_cut, list_device

def crossover_chromosomes(id, individual_adam, individual_eva):

    individual_son0 = copy.deepcopy(individual_adam)
    individual_son1 = copy.deepcopy(individual_eva)

    list_target0 = individual_son0.get_list_target()
    list_device0 = individual_son0.get_list_device()

    list_target1 = individual_son1.get_list_target()
    list_device1 = individual_son1.get_list_device()

    num_target = len(list_target0)

    for i in range (0, 5):
        
        x = random.randint (0,num_target-1)
        y = random.randint (0,num_target-1)
        target0 = list_target0[x]
        target1 = list_target1[y]
        list_target = [target1, target0]
        # cut trip
        list_cut0, list_device0 = cut_trips(target0, list_device0)
        list_cut1, list_device1 = cut_trips(target1, list_device1)

        #append trip
        i=-1
        for trips , target, list_device in zip([list_cut0,list_cut1],[target1, target0], [list_device1, list_device0]):
            i+=1
            target = list_target[i]
            if trips != []:
                for trip in trips:
                    target.add_trip(trip)

                    # chinh sua ben device 
                    id_device = trip[0]
                    list_device[id_device].append_target([target.get_id(), trip[1]])
                    


    new_individual0 = Individual(id-1, list_device0,  list_target0)
    new_individual1 = Individual(id,list_device1, list_target1)

    return new_individual0, new_individual1