
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

    def append_turn(self,info, id_trip = -1, id_turn = -1):
        try:
            if id_turn == -1:
                self.trips[id_trip].append(info)
            else:
                new_trip = []
                trip = self.trips[id_trip]
                new_trip = trip[:id_turn]
                new_trip.append(info)
                for turn in trip[id_turn:]:
                    new_trip.append(turn)
                self.trips[id_trip] = new_trip
        except:
            self.trips.append([])
            self.trips[0].append(info)

    def update_trip(self, id_target, numerical, new_weight_package ):
        '''
        INPUT: 
            id_target: id cua target mua thay doi
            numerical: so thu tu cua target day trong trip cua device 
            weight_package: trong luong cua goi hang moi 
        '''
        
        count = -1
        break_now = False
        
        for j in  range(0,len(self.trips)):
            for i in range (0,len(self.trips[j])):
                id = self.trips[j][i][0]
                if id == id_target:
                    count += 1
                if count == numerical:
                    self.trips[j][i][1] = new_weight_package
                    break_now = True

                if break_now:
                    break
            if break_now:
                break   

    def pop_turn(self, turn):
        index_turn =hex(id(turn))
        for i in  range(0, len(self.trips)):
            trip = self.trips[i]
            for j in range(0, len(trip)):
                turn = trip[j]
                index_tmp = hex(id(turn))
            
                if index_tmp == index_turn:
                    trip.pop(j)

                    if len(trip) == 0:
                        self.trips.pop(i)

                    return True


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
   
