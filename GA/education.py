from calculator.weight import sum_weight
from util.load_data import load_list_device
from util.show import show_info_individual

# get list left over
def get_llo_target(list_target, list_device):
    new_list_target = []
    new_list_device = []
    
    list_lo_ts = [] #list_left over in target
    list_target_wait = [[],[]]
    for target in list_target:

        id_target = target.get_id()
        trips = target.get_trip()
        lower_bound, upper_bound = target.get_bound_base()
        new_trips = []
        sum_bound = 0

        dic_device = {}
        for id_device, bound in trips:

            device = list_device[id_device]
            if id_device in dic_device:
                dic_device[id_device] += 1
            else:
                dic_device[id_device] = 0

            # neu vuot qua upper bound
            if sum_bound + bound > upper_bound:
                bound_ac = max(0, upper_bound - sum_bound)
                bound_lo = bound - bound_ac
                numerical = dic_device[id_device]

                if bound_ac != 0:
                    new_trips.append([id_device, bound_ac])

                    #cap nhap thong tin cho thiet bi
                    device.update_trip(id_target, numerical, bound_ac )
                    

                list_lo_ts.append([id_device, bound_lo])
                device.append_target([id_target, bound_lo], type = -1)

                sum_bound += bound_ac
                    
            else: 
                sum_bound += bound
                new_trips.append([id_device, bound])
        target.change_list_trip(new_trips)     
            
        # neu khong vuot qua lower bound
        if sum_bound < lower_bound:
            list_target_wait[0].append([id_target, sum_bound])    
        # neu lower_bound < bound < upper bound
        elif sum_bound < upper_bound:
            list_target_wait[1].append([id_target, sum_bound])

    return list_lo_ts, list_target_wait


def distribution_llo_target(list_lo_ts, list_target_wait, list_target, list_device):
    for id_target_wait, sum_bound in list_target_wait[0]:
        if len(list_lo_ts) == 0:
            break

        target = list_target[id_target_wait]
        lower_bound, upper_bound = target.get_bound_base()

        for i in range (0, len(list_lo_ts)):
            id_device, bound=  list_lo_ts[i]
            target.add_trip([id_device, bound])
            sum_bound += bound
            list_lo_ts.pop(i) 

            if sum_bound > lower_bound:
                break
    
    for id_target_wait, sum_bound in list_target_wait[1]:
        if len(list_lo_ts) == 0:
            break

        target = list_target[id_target_wait]
        lower_bound, upper_bound = target.get_bound_base()

        for i in range (0, len(list_lo_ts)):
            id_device, bound=  list_lo_ts[i]
            target.add_trip([id_device, bound])
            sum_bound += bound
            list_lo_ts.pop(i) 

            if sum_bound > upper_bound:
                break
    


def fix_target(list_target, list_device):

    list_lo_ts, list_target_wait = get_llo_target(list_target, list_device)
    #distribution_llo_target(list_lo_ts, list_target_wait, list_target, list_device)

    return list_target, list_device

# def fix_device(list_target, list_device):
#     pass

def processing(individual, matrix_distance):
    
    list_target = individual.get_list_target()
    list_device = individual.get_list_device()

    # xu ly target
    list_target, list_device = fix_target(list_target, list_device)
    
    # xu ly thiet bi
    # list_target, list_device = fix_device(list_target, list_device)

    individual.update_individual(list_device, list_target)


def education(population, matrix_distance):
    new_population = []
    # education tung ca the

    for individual in population:
        processing(individual, matrix_distance)
        show_info_individual(individual, text= "education")
        new_population.append(individual)
    return new_population