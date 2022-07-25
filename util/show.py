from cProfile import label
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from calculator.fitness_and_point import sum_fitness, sum_point
from config import NUM_DRONE

def showHistogram(list_target):
    list_lable = []
    list_cordinate = []
    for target in list_target:
        cordinate = target.get_cordinate()
        list_cordinate.append(cordinate)

    '''
    input: coordinates (x,y)
    output: map of point
    '''
    x=[]
    y=[]

    #depot
    x.append(0)
    y.append(0)

    for target in list_cordinate:
        x.append(target[0])
        y.append(target[1])

    plt.title("Cordinate")

    plt.xlabel("Value X")

    plt.ylabel("Value Y")

    plt.plot(x, y, "go")

    plt.show()

def show_info_target(list_target):
    for target in list_target:
        print("Target (ID: {}) co trip la: {}".format(target.get_id(), target.get_trip() ))
def show_info_device(list_device):
    for device in list_device:
        try:
            trip = device.get_trip()
        except:
            trip = device.get_trips()
        print("Device (ID: {}) co trip la: {}".format(device.get_id(), trip))

def show_info_individual(individual, text):

    print("\n \t \t <-<-<-<-<-<-<-<-<{}>->->->->->->->->".format(text))
    print("+ ID:      {}".format(individual.get_id()))
    print("+ Point:   {}".format(individual.get_point()))
    print("+ Fitness: {}".format(individual.get_fitness()))
    print("\n+ Info list target: ")

    list_target = individual.get_list_target()

    for target in list_target:
        print("\n \t target (ID {}):".format(target.get_id()), end='')

        for turn in target.get_trip():
            print("[{},{}]".format(turn.get_device(), turn.get_bound()), end='')

    print("\n+ Info list device:")
    list_device = individual.get_list_device()
    for device in list_device:
        print("\t device (ID :{}):".format(device.get_id()),end='')
        print("[",end='')
        if device.get_id()<NUM_DRONE:
            trips = device.get_trips()
            
            for trip in trips:
                print("[",end='')
                for turn in trip:
                    id_target = turn.get_target()
                    bound = turn.get_bound()
                    print("[{},{}]".format(id_target, bound), end='')
                print("]",end='')
            
        else:
            trip = device.get_trip()
            for turn in trip:
                id_target = turn.get_target()
                bound = turn.get_bound()
                print("[{},{}]".format(id_target, bound), end='')
        print("]")
def show_info_population(population, type):
    print("+ So quan the tao ra: {}".format(len(population)))
    print("+ Tong ham muc tieu: {}".format(sum_point(population)))
    print("+ Tong fitness: {}". format(sum_fitness(population)))
    if type != "mini":
        print("(v.v)")
        show_info_individual(population[0], "Ca the tot nhat" )

    else:
        print("Ca the tot nhat point {}, fitness {}".format( population[0].get_point(), population[0].get_fitness()))