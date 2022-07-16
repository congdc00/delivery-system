def processing(individual, matrix_distance):
    
    # xu ly target
    list_target = individual.get_list_target()
    

def education(population,matrix_distance):
    new_population = []

    for individual in population:
        new_individual = processing(individual, matrix_distance)
        new_population.append(new_individual)
    return new_population