
import random
import copy

import sys
from config import NUM_DRONE, NUM_TRUCK

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual

def choice_mutate(population):
    
    num_individual = len(population)-1
    random_number = random.randint(0,num_individual)

    return population[random_number]

def mutate_chromosomes(id, individual):

    new_individual = copy.deepcopy(individual)
    list_target = new_individual.get_list_target()
    for j in range(0,len(list_target)):

        target = list_target[j]
        trip = target.get_trip()

        # dot bien
        dict = {}
        for turn in trip:

            tmp = random.random()

            if tmp<0.4:
                bound = turn.get_bound()
                weight_package = bound + random.randint(1,50)
                turn.update_bound(weight_package)

    return new_individual