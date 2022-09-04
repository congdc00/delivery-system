import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')
from object.individual import Individual

def copy_individual(id, individual):
    status = individual.get_status()
    list_device = individual.get_list_device()
    list_target = individual.get_list_target()
    new_individual = Individual(id, list_device, list_target)
    new_individual.update_status(status)
    return new_individual