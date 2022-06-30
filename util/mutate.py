
import random
def choice_list_mutate(probability):
    list_crossover = []

    for i in range (0, len(probability)):
        tmp = random.random()
        if tmp<0.3:
            list_crossover.append(i)
	
    return list_crossover

def mutate_chromosomes(individual):
    list_trip = individual.get_info_target()
    print("list trip :{}".format(list_trip))
    for trip in range (0, len(list_trip)):
        for i in range(0, len(list_trip[trip])):
            weight = list_trip[trip][i][1]
            mutatio_weight = int(weight) + random.randint(1,10)
            list_trip[trip][i][1] = mutatio_weight

    individual.update_info_target(list_trip)
    
    return individual