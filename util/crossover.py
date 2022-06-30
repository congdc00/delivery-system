from config import SIZE_CROSSOVER
import random

def choice_list_crossover(probability):
    list_index_tmp= []
    list_index_crossover = []
    while len(list_index_tmp) < SIZE_CROSSOVER:
        for i in range (0, len(probability)):
            tmp = random.random()
            if tmp<0.5:
                list_index_tmp.append(i)
                if len(list_index_tmp) == SIZE_CROSSOVER:
                    break

    for i in range(0, len(list_index_tmp), 2):
        list_index_crossover.append([list_index_tmp[i], list_index_tmp[i+1]])
    
    return list_index_crossover

def crossover_chromosomes(couple_choice, population):

    '''
    Nên chọn 2 thằng nào có sự khác biệt nhất để lai ghép
    '''

    index_adam = couple_choice[0]
    adam = population[index_adam]
    list_trip_adam = adam.get_info_target()

    index_eva = couple_choice[1]
    eva = population[index_eva]
    list_trip_eva = eva.get_info_target()

    #cut trip
    list_cut_adam = []
    for index_trip in range (0,len(list_trip_adam)):
        trip = list_trip_adam[index_trip]
        k = random.randint(0, len(trip))

        #cat trip ra
        list_cut_tmp = []
        for i in range (k, len(trip)):
            list_cut_tmp.append(list_trip_adam[index_trip].pop(k))

        list_cut_adam.append(list_cut_tmp)
        
    list_cut_eva = []
    for index_trip in range (0,len(list_trip_eva)):
        trip = list_trip_eva[index_trip]
        k = random.randint(0, len(trip))

        #cat trip ra
        list_cut_tmp = []
        for i in range (k, len(trip)):
            list_cut_tmp.append(list_trip_eva[index_trip].pop(k)) 
        
        list_cut_eva.append(list_cut_tmp)

    # noi trip vao
    for index_trip in range (0,len(list_trip_adam)):
        new_trip = list_cut_adam[index_trip]
        list_trip_adam[index_trip].append(new_trip)

    adam.update_info_target(list_trip_adam)

    for index_trip in range (0,len(list_trip_eva)):
        new_trip = list_cut_eva[index_trip]
        list_trip_eva[index_trip].append(new_trip)

    eva.update_info_target(list_trip_eva)

    return adam, eva 