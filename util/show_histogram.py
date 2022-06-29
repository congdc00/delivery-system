from cProfile import label
import matplotlib.pyplot as plt

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