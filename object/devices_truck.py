
import sys

sys.path.append('/home/congdc/project/scheduled-delivery')

from config import NUM_DRONE

class Truck():

    def __init__(self,id,  speed, capacity, working_time):
        
        self.id = id
        self.speed = speed

        #base
        self.capacity_base = capacity
        self.working_time_base = working_time

        #now
        self.capacity = capacity
        self.working_time = working_time

    #working time
    def update_time(self, used_time):
        self.working_time -= used_time

    def update_capacity(self, weight_package):
        self.capacity -= weight_package

    def reset_capacity(self):
        self.capacity = self.capacity_base

    def get_capacity(self):
        return self.capacity
    
    def get_speed(self):
        return self.speed

    def get_working_time(self):
        return self.working_time

    #capacity
    def drop_down(self, weight_package):
        self.capacity -= weight_package
    
    def reset_capacity(self):
        self.capacity = self.capacity_base

    def get_capacity(self):
        return self.capacity

    def get_id(self):
        return self.id

def create_list_truck(num_truck, info_truck_base):
    '''
    Tạo danh sách các thiết bị truck
    '''
    # Khoi tao danh sach drone
    list_truck = []
    speed = info_truck_base[0]
    capacity= info_truck_base[1]
    working_time= info_truck_base[2]

    for i in range (NUM_DRONE, num_truck + NUM_DRONE):
        new_truck = Truck(i, speed, capacity, working_time) 
        list_truck.append(new_truck)

    return list_truck

# test
if __name__ == "__main__":
    test = "Truck"
    if test == "Truck":
        truck1 = Truck(0, 0.4, 1500, 60)
        truck2 = Truck(1, 0.4, 1500, 60)
        list_truck = []
        list_truck.append(truck1)
        list_truck.append(truck2)
        list_truck[1].drop_down(25)
        list_truck[0].drop_down(12)
        print(list_truck[0].get_capacity())
    else:
        info = [0.6, 40, 30, 60]
        list_drone = create_list_drone(2, info)
        list_drone[1].drop_down(39)
        print(list_drone[1].get_id())
   
