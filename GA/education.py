from turtle import update
from calculator.weight import sum_weight
from util.load_data import load_list_device
from util.show import show_info_individual, show_info_target, show_info_device



def fix_target(list_target, list_device):
    for target in list_target:
        weight_delivered = target.get_weight_delivered()
        lower_bound, upper_bound = target.get_bound_base()
        list_turn = target.get_trip()
        if weight_delivered<lower_bound:
            add_weight = lower_bound - weight_delivered
            turn = list_turn[0]
            weight_turn = turn.get_bound()
            new_weight = weight_turn + add_weight
            turn.update_bound(new_weight)


def fix_device(list_target, list_device):

    return True

def processing(individual, matrix_distance):
    
    list_target = individual.get_list_target()
    list_device = individual.get_list_device()

    # xu ly target
    fix_target(list_target, list_device)
    
    # xu ly thiet bi
    fix_device(list_target, list_device)


def education(population, matrix_distance):
    # education tung ca the

    for individual in population:
        processing(individual, matrix_distance)
    return population