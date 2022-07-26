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
    sum_f,_ = sum_fitness(population)
    print("+ Tong fitness: {}". format(sum_f))
    if type != "mini":
        print("(v.v)")
        show_info_individual(population[0], "Ca the tot nhat" )

    else:
        print("Ca the tot nhat point {}, fitness {}".format( population[0].get_point(), population[0].get_fitness()))

def show_histogram(fitness_log):
    fig1 = plt.gcf()
    plt.plot(fitness_log)
    plt.draw()
    fig1.savefig('log.png', dpi=100)

def show_map(individual):
    list_device = individual.get_list_device()
    list_target = individual.get_list_target()
    coordinate_all = []
    for device in list_device:
        id_device = device.get_id()
        coordinate_device = []
        if id_device < NUM_DRONE:
            trips = device.get_trips()
            for trip in trips:
                coordinate_device.append([0, 0])
                for turn in trip:
                    id_target = turn.get_target()
                    target = list_target[id_target]
                    cor_tmp = target.get_coordinate()
                    coordinate_device.append(cor_tmp)
                coordinate_device.append([0, 0])
        else:
            trip = device.get_trip()
            coordinate_device.append([0, 0])
            for turn in trip:
                id_target = turn.get_target()
                target = list_target[id_target]
                cor_tmp = target.get_coordinate()
                coordinate_device.append(cor_tmp)
            coordinate_device.append([0, 0])

        coordinate_all.append(coordinate_device)

    fig2 = plt.gcf()
    coordinate_x = [x[0] for x in coordinate_all[0]]
    coordinate_y = [y[1] for y in coordinate_all[0]]
    plt.plot(coordinate_x, coordinate_y, 'go-', label='Drone 0')

    coordinate_x = [x[0] for x in coordinate_all[1]]
    coordinate_y = [y[1] for y in coordinate_all[1]]
    plt.plot(coordinate_x, coordinate_y, 'ro-', label='Drone 1')

    coordinate_x = [x[0] for x in coordinate_all[2]]
    coordinate_y = [y[1] for y in coordinate_all[2]]
    plt.plot(coordinate_x, coordinate_y, 'bo-', label='Truck 2')

    coordinate_x = [x[0] for x in coordinate_all[3]]
    coordinate_y = [y[1] for y in coordinate_all[3]]
    plt.plot(coordinate_x, coordinate_y, 'yo-', label='Truck 3')
    plt.title('map')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='best')
    fig2.savefig('map.png', dpi=100)