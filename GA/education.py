from calculator.weight import sum_weight


def processing(individual, matrix_distance):
    
    list_scrap = []
    list_target_ready = []

    # xu ly target
    list_target = individual.get_list_target()
    for target in list_target:
        ready = True
        list_trip  = target.get_trip()
        lower_bound, upper_bound = target.get_bound()

        sum_bound = 0
        for i in range(0, len(list_trip)):
            if sum_bound + list_trip[i][1] <= upper_bound:
                sum_bound += list_trip[i][1]
            else:
                
                list_trip_pop, _ = target.pop_trip_from(i)

                list_trip_pop[0][1] = list_trip[i][1] - (upper_bound - sum_bound)
                list_trip[i][1] = upper_bound - sum_bound
                target.add_trip(list_trip[i])
                for trip in list_trip_pop:
                    list_scrap.append(trip)
                ready = False
                sum_bound = upper_bound
                break
        if ready:
            list_target_ready.append(target.get_id())
    
    for id_target in list_target_ready:
        target = list_target[id_target]
        ready = True
        list_trip  = target.get_trip()
        lower_bound, upper_bound = target.get_bound()

        sum_bound = 0
        #cac trip truoc
        for i in range(0, len(list_trip)):
            if sum_bound + list_trip[i][1] <= upper_bound:
                sum_bound += list_trip[i][1]

        # bo xung
        for i in range (0, list_scrap):
            if sum_bound + list_scrap[i][0]<=upper_bound:
                sum_bound += list_scrap[i][0]
                target.add_trip(list_scrap[i])
                list_scrap.pop(i)

        




def education(population,matrix_distance):
    new_population = []

    for individual in population:
        new_individual = processing(individual, matrix_distance)
        new_population.append(new_individual)
    return new_population