import numpy as np 
import random
import csv  

# khoi tao ham so ban dau
def initSet( num_drone,  num_truck,  num_target):
    #num drone
    m = num_drone

    #num truck
    k = num_truck

    #num target
    t = num_target

    # demand
    list_demand = np.random.randint(1, 10, (num_target, 1))

    # cordinate
    list_cordinate = np.random.randint(-20, 20, (num_target, 2))

    # low-bound
    list_min_bound = np.random.randint(1, 20, (num_target, 1))
    list_max_bound = []
    list_max_bound.append(list_min_bound+np.random.randint(1, 20, (13, 1)))


    return m,k,t, list_demand, list_cordinate, list_min_bound, list_max_bound

def initParameter():
    # km/h
    SPEEDK  = random.randint(1, 10)
    SPEEDM  = SPEEDK + random.randint(1, 10)

    #capacity drone
    W = random.randint(1, 10)

    #time drone
    d = random.randint(1, 20)

    #working time
    D = d + random.randint(20, 50)

    return SPEEDK, SPEEDM, W, d, D

def print_idata(m,k,t, list_demand, list_cordinate,  list_min_bound, list_delt, SPEEDK, SPEEDM, W, d, D):
    print("so luong drone: {}".format(m))
    print("toc do drone (km/h): {}".format(SPEEDM))
    print("tai trong toi da cua drone (kg): {}".format(W))
    print("gioi han thoi gian bay (h): {}".format(d))

    print("so luong xe tai: {}".format(k))
    print("toc do xe tai (km/h): {}".format(SPEEDK))

    print("so luong muc tieu: {}".format(t))

    print("gioi han thoi gian nhiem vu (h): {}".format(D))

    for i in range (0, t):
        print("------------------------")
        print("muc tieu so {}".format(i+1))
        print("toa do (x,y): ({},{})".format(list_cordinate[i][0],list_cordinate[i][1]))
        print("trong so: {}".format(list_demand[i][0]))
        print("khoi luong min: {}".format(list_min_bound[i][0]))
        print("khoi luong max: {}".format(list_max_bound[0][i][0]))

def save(m,k,t, list_demand, list_cordinate,  list_min_bound, list_max_bound, SPEEDK, SPEEDM, W, d, D):

    with open('data01.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        
        #drone
        writer.writerow([m])
        writer.writerow([SPEEDM])
        writer.writerow([W])
        writer.writerow([d])

        #truck
        writer.writerow([k])
        writer.writerow([SPEEDK])

        #target
        writer.writerow([t])

        #time
        writer.writerow([D])

        # write the data
        for i in range (0,t):
            writer.writerow([i +1 , list_demand[i][0], list_cordinate[i][0],list_cordinate[i][1], list_min_bound[i][0],list_max_bound[0][i][0]])

if __name__ == "__main__":

    random.seed(42)
    
    #khoi tao trong so
    m,k,t, list_demand, list_cordinate,  list_min_bound, list_max_bound = initSet(num_drone = 3, num_truck = 4, num_target = 13)
    SPEEDK, SPEEDM, W, d, D = initParameter()

    #show data
    print_idata(m,k,t, list_demand, list_cordinate,  list_min_bound, list_max_bound, SPEEDK, SPEEDM, W, d, D)

    #save data
    save(m,k,t, list_demand, list_cordinate,  list_min_bound, list_max_bound, SPEEDK, SPEEDM, W, d, D)

