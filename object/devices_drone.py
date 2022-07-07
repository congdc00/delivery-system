
class Drone():

    def __init__(self,id,  speed, capacity, duration, working_time):
        
        self.id = id
        self.speed = speed

        #base
        self.capacity_base = capacity
        self.duration_base = duration
        self.working_time_base = working_time

        #now
        self.capacity = capacity
        self.duration = duration
        self.working_time = working_time
        self.trips = []

    # SET
    def update_time(self, used_time):
        self.working_time -= used_time
        self.duration -= used_time

    def update_capacity(self, weight_package):
        self.capacity -= weight_package

    def drop_down(self, weight_package):
        self.capacity -= weight_package
    
    def reset_capacity(self):
        self.capacity = self.capacity_base

    def create_trip(self, new_trip):
        self.trips.append(new_trip)


    def update_trip(self, id_target, weight_package, index_trip, index_in_trip, type):
        if type == "append":
            new_trip = []

            begin = self.trips[index_trip][:index_in_trip]
            new_trip.append(begin)

            new_trip.append([id_target, weight_package])

            end = self.trips[index_trip][index_in_trip: ]
            new_trip.append(end)
            self.trips[index_trip] = new_trip
        else:
            self.trips[index_trip].pop(index_in_trip)
        


    # RESET lai khi ve kho
    def reset_duration(self):
        self.duration = self.duration_base

    def reset_capacity(self):
        self.capacity = self.capacity_base

    # GET
    def get_capacity(self):
        return self.capacity
    
    def get_speed(self):
        return self.speed

    def get_working_time(self):
        return self.working_time

    def get_duration(self):
        return self.duration

    def get_capacity(self):
        return self.capacity

    def get_id(self):
        return self.id

    def get_trips(self):
        return self.trips

def create_list_drone(num_drone, info_drone_base):
    '''
    Tạo danh sách các thiết bị drone
    '''
    # Khoi tao danh sach drone
    list_drone = []
    speed = info_drone_base[0]
    capacity= info_drone_base[1]
    duration= info_drone_base[2]
    working_time= info_drone_base[3]

    for i in range (0, num_drone):
        new_drone = Drone(i, speed, capacity, duration, working_time) 
        list_drone.append(new_drone)

    return list_drone

# test
if __name__ == "__main__":
    test = "create"
    if test == "Drone":
        drone1 = Drone(0.6, 40, 30, 60)
        drone2 = Drone(0.6, 40, 30, 60)
        list_drone = []
        list_drone.append(drone1)
        list_drone.append(drone2)
        list_drone[1].drop_down(25)
        list_drone[0].drop_down(12)
        print(list_drone[0].get_capacity())
    else:
        info = [0.6, 40, 30, 60]
        list_drone = create_list_drone(2, info)
        list_drone[1].drop_down(39)
        print(list_drone[1].get_id())
   
