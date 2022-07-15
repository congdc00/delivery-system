
import random
import copy

import sys
from config import NUM_DRONE

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual

def choice_mutate(population):
    
    num_individual = len(population)-1
    random_number = random.randint(0,num_individual)

    return population[random_number]

def mutate_chromosomes(id, individual):

    new_individual = copy.deepcopy(individual)
    list_target = new_individual.get_list_target()
    list_device = new_individual.get_list_device()
    for j in range(0,len(list_target)):

        target = list_target[j]
        list_trip = target.get_trip()
        id_target = target.get_id()

        # dot bien
        dict = {}
        new_list_trip = []
        for trip in list_trip:
            if trip[0] in dict:
                dict[trip[0]] += 1
            else:
                dict[trip[0]] = 0

            tmp = random.random()
            if tmp<0.4:
                id_device = trip[0]
                weight_package = trip[1] + random.randint(1,50)
                new_list_trip.append([id_device, weight_package])
                list_device[id_device].update_trip(id_target, dict[trip[0]], weight_package)

            else:
                new_list_trip.append([trip[0], trip[1] ])
                
        #gan lai
        target.change_list_trip(new_list_trip)
        new_individual.update_target(target, j)

    new_individual = copy_individual(id, new_individual)

    return new_individual