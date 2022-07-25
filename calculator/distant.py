
import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')
import math
from config import COORDINATES_DEPOT

def get_distant(cor_start, cor_end):
    x_start = cor_start[0]
    y_start = cor_start[1]
    x_end = cor_end[0]
    y_end = cor_end[1]

    distant = math.sqrt((x_start-x_end)**2 + (y_start-y_end)**2)

    return distant
def get_time(speed, cor_start, cor_end):
    distant = get_distant(cor_start, cor_end)
    time = distant/speed
    return time

def set_distant(depot, list_target):
    matrix_distance = []
    for i in range (0,len(list_target) + 1):
        
        id_start = i - 1
        if id_start == -1:
            target_start = depot
            cor_start = COORDINATES_DEPOT
        else:
            target_start = list_target[id_start]
            cor_start = target_start.get_coordinate()
        
        matrix_distance.append([])
        for j in range (0, len(list_target) + 1):

            id_end = j - 1

            if id_end == -1:
                cor_end = COORDINATES_DEPOT
            else:
                target_end = list_target[id_end]
                cor_end = target_end.get_coordinate()
            
            distant = get_distant(cor_start, cor_end)

            target_start.add_neighbor(id_end, distant)
            matrix_distance[i].append(distant)
        target_start.sort_neighbor()

        if id_start == -1:
            depot = target_start
        else:
            list_target[id_start] = target_start
    
    return depot, list_target, matrix_distance



    