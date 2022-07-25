
import random
import copy

import sys
from config import NUM_DRONE, NUM_TRUCK
from util.load_data import load_list_device

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual
from object.turn import Turn

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
        id_target = target.get_id()
        trip = target.get_trip()

        # dot bien
        dict = {}
        for turn in trip:

            tmp = random.random()

            if tmp<0.8:
                bound = turn.get_bound()
                weight_package = bound + random.randint(1,50)
                turn.update_bound(weight_package)

            else:
                weight = random.randint(0,10)
                id_device = random.randint(0, NUM_DRONE+NUM_TRUCK-1)
                device = list_device[id_device]
                turn = Turn(id_target, id_device, weight)
                target.add_turn(turn)

                if id_device < NUM_DRONE:
                    trips = device.get_trips()
                    num_trip = len(trips)
                    if num_trip != 0:
                        id_trip = random.randint(0, num_trip-1)
                    else:
                        id_trip = 0
                    device.append_turn(turn, id_trip)
                else:
                    device.append_turn(turn, type = -1)
    return new_individual