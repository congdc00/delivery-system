
from object.target import Target
from util import load_data 
from init.solution0 import init_solution0
from init.solution1 import init_solution1
from util.load_data import load_list_target, load_list_device
from calculator.distant import set_distant
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CHOICE
from calculator.fitness import get_fitness_and_point, sum_fitness
from GA.mutate import choice_mutate, mutate_chromosomes
from GA.crossover import choice_list_crossover, crossover_chromosomes, build_matrix_crossover_point
from GA.selection import selection_chromosomes



def find_best_individual(population):
    max_fitness = 0
    print("lay duoc fitness : {}".format(population[1].get_fitness()))
    for i in range(0,len(population)):
        print("tai index {}".format(i))
        fitness_i = population[i].get_fitness()
        if fitness_i> max_fitness:
            max_fitness = fitness_i
            index_max = i

    return population[index_max]


def create_param():
    #Khoi tao kho:
    depot = Target(-1, 0, 0, 0,0,0)
    
    #Khoi tao list target
    list_target = load_list_target(ROOT_PATH_DATA)
    depot, list_target = set_distant(depot, list_target)

    # Khoi tao hang doi drone va truck
    list_drone, list_truck = load_list_device()

    return depot, list_drone, list_truck, list_target

if __name__ == "__main__":

    

    list_solution_choice = [init_solution0, init_solution1]

    population = []

    index = -1
    for init_solution in list_solution_choice:
        index += 1

        depot, list_drone, list_truck, list_target = create_param()

        list_drone, list_truck, list_target = init_solution( list_drone, list_truck,depot, list_target )
        new_individual = Individual(index, list_drone, list_truck, list_target)
        population.append(new_individual)

    for i in range (0, 100):
        new_population = []
        
        #Chon thang tot nhat
        new_individual0 = find_best_individual(population)
        new_population.append(new_individual0)

        #Chon loc
        for j in range (0,1):
            individual_choice = selection_chromosomes(population)
            new_population.append(individual_choice)

        #Lai ghep
        for j in range (0, 1):
            matrix_crossover = build_matrix_crossover_point(population)
            individual_adam, individual_eva = choice_list_crossover(population, matrix_crossover, rank = 0)
            new_individual1, new_individual2 = crossover_chromosomes(individual_adam, individual_eva)
            new_population.append(new_individual1)
            new_population.append(new_individual2)

        #Dot bien
        for j in range (0,1):
            individual_choice = choice_mutate(population)
            new_individual = mutate_chromosomes(individual_choice)
            new_population.append(new_individual)

        population = []
        for individual in new_population:
            population.append(individual)
        
        print("so ca the trong quan the moi {}".format(len(population)))


   

    
