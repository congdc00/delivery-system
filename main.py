'''
su dung Genetic Algorithm
'''

from object.target import Target
from util import load_data 
from init.solution0 import init_solution0
from init.solution1 import init_solution1
from util.load_data import load_list_target, load_list_device
from calculator.distant import set_distant
from util.show import show_info_individual
from object.individual import Individual
from config import ROOT_PATH_DATA, POP_SIZE, SIZE_CHOICE
from calculator.fitness_and_point import sum_point, sum_fitness
from GA.mutate import choice_mutate, mutate_chromosomes
from GA.crossover import choice_list_crossover, crossover_chromosomes, build_matrix_crossover_point
from GA.selection import selection_chromosomes
from util.duplicate import copy_individual
    

def find_best_individual(id, population):
    max_point = 0
    for i in range(0,len(population)):
        point_i = population[i].get_point()
        if point_i> max_point:
            max_point = point_i
            index_max = i

    best_individual = copy_individual(id, population[index_max])
    return best_individual


def create_param():
    #Khoi tao kho:
    depot = Target(-1, 0, 0, 0,0,0)
    
    #Khoi tao list target
    list_target = load_list_target(ROOT_PATH_DATA)
    depot, list_target = set_distant(depot, list_target)

    # Khoi tao hang doi drone va truck
    list_device = load_list_device()

    return depot, list_device, list_target

if __name__ == "__main__":

  
    depot, list_device, list_target = create_param()  

    list_solution_choice = [init_solution0, init_solution1]

    # Tao init solution
    population = []
    index = -1
    for init_solution in list_solution_choice:
        index += 1
        new_list_device, new_list_target = init_solution( list_device, depot, list_target )
        new_individual = Individual(index, new_list_device, new_list_target)
        population.append(new_individual)

    show_info_individual(population[1], "tao individual")

    for i in range (0, 1):
        print("\t ------------------------------vong lap thu {} -----------------------------".format(i))
        
        
        new_population = []
        id = 0
        
        #Chon individual tot nhat
        best_individual = find_best_individual(id, population)
        new_population.append(best_individual)
        
        #Chon loc
        for j in range (0,2):
            id += 1
            individual_choice = selection_chromosomes(id, population)
            new_population.append(individual_choice)

        #Lai ghep
        for j in range (0, 1):
            id += 2
            matrix_crossover = build_matrix_crossover_point(population)
            
            individual_adam, individual_eva = choice_list_crossover(population, matrix_crossover, rank = j)
            show_info_individual(individual_adam, "individual_adam")
            show_info_individual(individual_eva, "individual_eva")
            new_individual1, new_individual2 = crossover_chromosomes(id, individual_adam, individual_eva)

            
            show_info_individual(new_individual1, "individual 1")
            show_info_individual(new_individual2, "individual 2")

            new_population.append(new_individual1)
            new_population.append(new_individual2)

            

        #Dot bien
        for j in range (0,1):
            id += 1
            individual_choice = choice_mutate(population)
            new_individual = mutate_chromosomes(id, individual_choice)
            new_population.append(new_individual)

       
        population = new_population
        


   

    
