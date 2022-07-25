
from operator import index
from turtle import width
from config import NUM_TRUCK, SIZE_CROSSOVER,NUM_DRONE
import random
import copy

import sys

from util.show import show_info_individual

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual
from util.find import find_device_by_id
from object.individual import Individual

def sum_difference(individual0, individual1):
    '''
    Ham tinh su khac biet giua hai ca the
    status == 0 la duoi lower bound
    status == 1 la tren lower bound
    status == 2 la dat upper bound
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
                    point_crossover = matrix_crossover[i][j]

        i = index_best_choice[0]
        j = index_best_choice[1]
    else:                
        i = random.randint(0, len(population)-1)    
        j = random.randint(0, len(population)-1)     

    return population[i], population[j]

    
    
    

def cut_trips(target, list_device):
    '''
    cat trip tu mot diem bat ky
    OUTPUT = 
    '''
    list_trip = target.get_trip()
    num_trip = len(list_trip)
    try:
        num_start_choice = random.randint(0,num_trip-1)
        if num_start_choice != num_trip-1:
            num_end_choice = random.randint(num_start_choice,num_trip-1)
        else:
            num_end_choice = random.randint(num_start_choice,-1)
    except:
        return [], list_device
        
    list_cut = target.pop_trip_from(num_start_choice,num_end_choice)

    # cap nhap lai device
    if len(list_cut) != 0:
        for turn in list_cut:
            id_device = turn.get_device()
            list_device[id_device].pop_turn(turn)

    return list_cut, list_device

def crossover_target(id, individual_adam, individual_eva):
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

        # cut trip
        
        list_cut0, list_device0 = cut_trips(target0, list_device0)
        print("target {} cat ra duoc : {}".format(x, list_cut0))
        list_cut1, list_device1 = cut_trips(target1, list_device1)
        print("target {} cat ra duoc : {}".format(y, list_cut1))

        
        
        #append trip
        for turns , target, list_device in zip([list_cut0,list_cut1],[target1, target0], [list_device1, list_device0]):
            
            id_target = target.get_id()
            
            if turns != []:
                for turn in turns:
                    #noi turn vao target moi
                    list_turn = target.get_trip()
                    num_turn = len(list_turn)
                    lucky_num = random.randint(0, num_turn)
                    target.add_turn(turn, index = lucky_num)
                    turn.update_target(id_target)

                    # chinh sua ben device 
                    id_device = turn.get_device()
                    print(" [{},{}] noi vao target  {}".format(turn.get_device(), turn.get_bound(), id_target))
                    device = list_device[id_device]

                    if id_device < NUM_DRONE:
                        trips = device.get_trips()
                        num_trips = len(trips)
                        try:
                            id_trip_choice = random.randint(0, num_trips-1)
                        except:
                            id_trip_choice = 0 
                        trip = trips[id_trip_choice]
                        num_turn = len(trip)
                        try:
                            id_turn_choice = random.randint(0, num_turn-1)
                        except:
                            id_turn_choice = 0
                        device.append_turn(turn, id_trip = id_trip_choice, id_turn = id_turn_choice)
                    else:
                        trip = device.get_trip()
                        num_turn = len(trip)
                        try:
                            id_turn_choice = random.randint(0, num_turn-1)
                        except:
                            id_turn_choice = 0
                        device.append_turn(turn, id_turn = id_turn_choice)

                    
    new_individual0 = Individual(id-1, list_device0,  list_target0)
    new_individual1 = Individual(id,list_device1, list_target1)
    return new_individual0, new_individual1 

def crossover_device(id, individual_adam, individual_eva):
    individual_son0 = copy.deepcopy(individual_adam)
    individual_son1 = copy.deepcopy(individual_eva)

    list_target0 = individual_son0.get_list_target()
    list_device0 = individual_son0.get_list_device()

    list_target1 = individual_son1.get_list_target()
    list_device1 = individual_son1.get_list_device()

    for i in range(0, 5):
        id_device_adam = random.randint(0, NUM_DRONE+NUM_TRUCK - 1)
        device_adam = list_device0[id_device_adam]

        id_device_eva = random.randint(0, NUM_DRONE+NUM_TRUCK - 1)
        device_eva = list_device0[id_device_eva]


    new_individual0 = Individual(id-1, list_device0,  list_target0)
    new_individual1 = Individual(id,list_device1, list_target1)
    return new_individual0, new_individual1 

def crossover_chromosomes(id, individual_adam, individual_eva):

    lucky_num = random.random()
    if lucky_num <= 2:
        new_individual0, new_individual1 = crossover_target(id, individual_adam, individual_eva)
    # else:
    #     new_individual0, new_individual1 = crossover_device(id, individual_adam, individual_eva)
    
    return new_individual0, new_individual1