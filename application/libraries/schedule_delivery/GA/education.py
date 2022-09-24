from turtle import update
from calculator.weight import sum_weight
from config import CAP_DRONE, CAP_TRUCK, NUM_DRONE, NUM_TRUCK
from util.load_data import load_list_device
from util.show import show_info_individual, show_info_target, show_info_device
import random
from object.turn import Turn

def choice_device(target, list_device): 

    min_working_time = 0
    index_device = -1
    list_turn =  target.get_trip()

    if len(list_turn) == 0:
        return -1

    list_device_ava = []
    list_first = []
    count = -1
    for turn in list_turn:
        count += 1
        id_device = turn.get_device()
        if id_device not in list_device_ava:
            list_device_ava.append(id_device)
            list_first.append(count)

    count = -1
    for id_device in list_device_ava:
        count += 1
        device = list_device[id_device]
        working_time = device.get_working_time()
        if min_working_time < working_time:
            save_count = count

    return list_first[save_count]

    

def fix_target(list_target, list_device):
    for target in list_target:
        weight_delivered = target.get_weight_delivered()
        lower_bound, upper_bound = target.get_bound_base()
        list_turn = target.get_trip()
        if weight_delivered<lower_bound:
            add_weight = lower_bound - weight_delivered
            index_turn_choice = choice_device(target, list_device)
            if index_turn_choice != -1:
                # print('bo xung them cho target {}'.format(target.get_id()))
                turn = list_turn[index_turn_choice]
                weight_turn = turn.get_bound()
                new_weight = weight_turn + add_weight
                turn.update_bound(new_weight)
            
                


def fix_device( list_device):

    for device in list_device:
        id_device = device.get_id()
        if id_device < NUM_DRONE:
            trips = device.get_trips()
            for trip in trips:
                sum_weight = 0
                max_weight = 0
                id_max_weight = 0
                count = -1
                for turn in trip:
                    weight = turn.get_bound()
                    sum_weight += weight
                    count += 1
                    if weight > max_weight:
                        max_weight = weight
                        id_max_weight = count
                
                if sum_weight > CAP_DRONE:
                    turn = trip[id_max_weight]
                    
                    if sum_weight - CAP_DRONE >= turn.get_bound():
                        turn.update_bound(1)
                    
                    else:
                        turn.update_bound( turn.get_bound() - (sum_weight - CAP_DRONE))

        else:
            trip = device.get_trip()
            sum_weight = 0
            max_weight = 0
            id_max_weight = 0
            count = -1
            for turn in trip:
                weight = turn.get_bound()
                sum_weight += weight
                count += 1
                if weight > max_weight:
                    max_weight = weight
                    id_max_weight = count
            
            if sum_weight > CAP_TRUCK:
                turn = trip[id_max_weight]
                
                if sum_weight - CAP_TRUCK >= turn.get_bound():
                    turn.update_bound(1)
                    
                else:
                    turn.update_bound(turn.get_bound() - (sum_weight - CAP_TRUCK))



def processing(individual, matrix_distance):
    
    list_target = individual.get_list_target()
    list_device = individual.get_list_device()

    # xu ly target
    fix_target(list_target, list_device)
    
    # xu ly thiet bi
    # show_info_individual(individual, text="truoc khi education")
    fix_device(list_device)
    # show_info_individual(individual, text="sau khi education")


def education(population, matrix_distance):
    # education tung ca the

    for individual in population:
        fitness = individual.get_fitness()
        if fitness < -30:
            processing(individual, matrix_distance)
        
    return population