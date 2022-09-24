from cProfile import label
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/dinhchicong/Project/delivery-system/back_end/schedule_delivery')

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
    plt.plot(coordinate_x, coordinate_y, 'go--', label='Drone 0')

    coordinate_x = [x[0] for x in coordinate_all[1]]
    coordinate_y = [y[1] for y in coordinate_all[1]]
    plt.plot(coordinate_x, coordinate_y, 'ro--', label='Drone 1')

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

def show_mix_histogram(list_log):

    lst = ['solid','dotted','dashed','dashdot','-',(0, (1, 10)),(0, (1, 1)),(0, (1, 1))]
    cs = ['b','g','r','c','m','y','k']
    mk = ['.','o','v','^','<','>','s']
    fig3 = plt.gcf()
    count = 0
    for log in list_log:
        plt.plot(log, color=cs[count], label = "k = 0."+str(int(count)+3))
        count += 1

    plt.title('Trên bộ dữ liệu 20.5.1')
    plt.xlabel('Số vòng lặp')
    plt.ylabel('Fitness')
    plt.legend(loc='best')
    fig3.savefig('mix.png', dpi=100)

if __name__ == "__main__":
    # loại 60-60-40
    #0.6
    #log_1 = [0.9055555555555556, 0.9055555555555556, 0.9055555555555556, 0.9055555555555556, 0.9055555555555556, 0.9055555555555556, 0.9065925925925926, 0.9065925925925926, 0.9065925925925926, 0.9246666666666666, 0.9279259259259259, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.9362222222222222, 0.963925925925926, 0.963925925925926, 0.963925925925926, 0.963925925925926, 0.963925925925926, 0.963925925925926, 0.9732592592592593, 0.9732592592592593, 0.9732592592592593, 0.9732592592592593, 0.9732592592592593, 0.9732592592592593, 0.9822962962962963, 0.9822962962962963, 0.9842962962962963, 0.9842962962962963, 0.9842962962962963, 0.9842962962962963, 0.9842962962962963, 0.9842962962962963, 0.9842962962962963, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481, 0.9861481481481481]
    #0.5 
    #log_2 = [0.9055555555555556, 0.9055555555555556, 0.9055555555555556, 0.928074074074074, 0.928074074074074, 0.928074074074074, 0.928074074074074, 0.928074074074074, 0.9307407407407408, 0.9307407407407408, 0.9528148148148148, 0.9528148148148148, 0.9528148148148148, 0.9528148148148148, 0.9528148148148148, 0.9528148148148148, 0.9622962962962963, 0.9622962962962963, 0.9622962962962963, 0.9641481481481482, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629, 0.9729629629629629]
    
    
    #loai 20-40-20
    #0.3
    log_0 = [0.9294117647058824, 0.9475764705882352, 0.9475764705882352, 0.9475764705882352, 0.9475764705882352, 0.9475764705882352, 0.9475764705882352, 0.9475764705882352, 0.9480470588235295, 0.9480470588235295, 0.9539764705882353, 0.9555764705882352, 0.9727058823529412, 0.982964705882353, 0.982964705882353, 0.982964705882353, 0.982964705882353, 0.982964705882353, 0.982964705882353, 0.982964705882353, 0.9833411764705883, 0.9833411764705883, 0.9833411764705883, 0.9833411764705883, 0.9833411764705883, 0.9833411764705883, 0.9844705882352941, 0.9856941176470588, 0.9924705882352941, 0.9924705882352941, 0.9924705882352941, 0.9924705882352941, 0.9924705882352941, 0.9948235294117647, 0.9948235294117647, 0.9948235294117647, 0.9948235294117647, 0.9948235294117647, 0.995764705882353, 0.9971764705882353, 0.9971764705882353, 0.9972705882352941, 0.9972705882352941, 0.9972705882352941, 0.9995294117647059, 0.9995294117647059, 0.9995294117647059, 1.0, 1.0, 1.0]
    #0.4
    log_1 = [0.9294117647058824, 0.9294117647058824, 0.9316705882352941, 0.9558588235294118, 0.9558588235294118, 0.9558588235294118, 0.9573647058823529, 0.966964705882353, 0.966964705882353, 0.9693176470588235, 0.9693176470588235, 0.9861647058823529, 0.9861647058823529, 0.9906823529411765, 0.9959529411764706, 0.9959529411764706, 0.9959529411764706, 0.9959529411764706, 0.9968941176470588, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    #0.5
    log_2 = [0.9294117647058824, 0.9388235294117647, 0.9403294117647059, 0.9468235294117647, 0.9468235294117647, 0.9487058823529412, 0.9487058823529412, 0.9635764705882353, 0.9650823529411765, 0.9664, 0.9664, 0.9664, 0.9687529411764706, 0.9712941176470589, 0.9779764705882353, 0.9821176470588235, 0.9830588235294118, 0.9830588235294118, 0.990964705882353, 0.990964705882353, 0.990964705882353, 0.9933176470588235, 0.9952941176470588, 0.9952941176470588, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    #0.6
    log_3 = [0.9294117647058824, 0.9294117647058824, 0.9294117647058824, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9476705882352942, 0.9785411764705882, 0.9785411764705882, 0.9785411764705882, 0.9785411764705882, 0.9785411764705882, 0.9785411764705882, 0.9917176470588235, 0.9917176470588235, 0.9917176470588235, 0.9917176470588235, 0.9917176470588235, 0.9917176470588235, 0.9917176470588235, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9936, 0.9943529411764706, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294, 0.9976470588235294]
    #0.7
    log_4 = [0.9294117647058824, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.9424, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588, 0.9856941176470588]
    list_log = [log_0,log_1, log_2, log_3, log_4]
    show_mix_histogram(list_log)