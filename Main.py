from curses.ascii import SO
from os import makedirs
import numpy as np 
import csv
import matplotlib.pyplot as plt

def readdata():
    with open('.\data\id_cong.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        list_param = []
        list_target = []
        for row in csv_reader:
            if line_count < 8:
                list_param.append(int(row[0]))
            else:
                list_tmp = []
                for i in range (0,6):
                    list_tmp.append(int(row[i]))
                list_target.append(list_tmp)

            line_count += 1
        return list_param,list_target

def showHistogram(x, y):
    '''
    
    '''
    plt.title("Cordinate")

    plt.xlabel("Value X")

    plt.ylabel("Value Y")

    plt.plot(x, y, "go")

    plt.show()

if __name__ == "__main__":

    list_param,list_target = readdata()
    m, SPEEDM, W, d, k, SPEEDK, t, D = list_param
    x=[]
    y=[]
    x.append(0)
    y.append(0)

    for target in list_target:
        x.append(target[2])
        y.append(target[3])

    showHistogram(x, y)


    