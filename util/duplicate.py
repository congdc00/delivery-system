import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')
from object.individual import Individual

def copy_individual(id, individual):
    list_drone = individual.get_list_drone()
    list_truck = individual.get_list_truck()
    list_target = individual.get_list_target()
    new_individual = Individual(id, list_drone, list_truck, list_target)
    return new_individual