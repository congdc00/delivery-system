
from unittest import result



def take_second(elem):
    return elem[1]
class Target():
    def __init__(self,id,x,y,lower_bound, upper_bound, weight):

        #self.penalty = penalty
        self.id =id
        self.x = x
        self.y = y 
        self.status = 0
        self.lower_bound = lower_bound
        self.lower_bound_base = lower_bound
        self.upper_bound = upper_bound
        self.upper_bound_base =upper_bound
        self.list_trip = []
        self.list_neighbor = []

        #trong so
        self.weight = weight
    
    #SET
    def update_bound(self, weight_package, type):
        '''
        Cập nhập lower bound và uppper bound 
        INPUT: 
        weight_package = khối lượng gói hàng
        type = 1 nếu gói hàng là được nhận
        type = 0  nếu gói hàng là được lấy đi
        '''
        if type == 1:
            self.lower_bound -= weight_package
            self.upper_bound -= weight_package
        if type == 0:
            self.lower_bound += weight_package
            self.upper_bound += weight_package

        if self.upper_bound <=0:
            self.status = 2
        elif self.lower_bound <= 0:
            self.status = 1
        else:
            self.status = 0


    def add_turn(self, new_component, index = -1):
        if index == -1:
            self.list_trip.append(new_component)
        else: 
            self.list_trip = self.list_trip[:index] + [new_component] + self.list_trip[index:]

    def change_list_trip(self, new_trip):
        self.list_trip = new_trip

        
    def pop_trip_from(self, num_start_choice, num_end_choice):
        if num_end_choice != -1:
            # tao trip con tach ra tu index
            list_trip_pop = self.list_trip[num_start_choice:num_end_choice]

            # cat trip
            self.list_trip = self.list_trip[:num_start_choice] + self.list_trip[num_end_choice:]
        else:
            list_trip_pop = self.list_trip[num_start_choice:]
            self.list_trip = self.list_trip[:num_start_choice]
        
        return list_trip_pop
        
    def add_neighbor(self,id, distant):
        self.list_neighbor.append([id, distant])
    
    def sort_neighbor(self):
        list_neighbor = self.list_neighbor
        list_neighbor_sorted = sorted(list_neighbor, key=take_second)
        self.list_neighbor = list_neighbor_sorted


    # GET  
    def get_weight(self):
        return self.weight

    def get_weight_delivered(self):
        sum_weight = 0
        for turn in self.list_trip:
            bound = turn.get_bound()
            sum_weight += bound

        return sum_weight
        
    def get_status(self):
        return self.status
    
    def get_weight_delivered(self):
        return self.lower_bound_base - self.lower_bound

    def get_bound(self):
        return self.lower_bound, self.upper_bound

    def get_bound_base(self):
        return self.lower_bound_base, self.upper_bound_base

    def get_coordinate(self):
        return [self.x, self.y]
    
    def get_id(self):
        return self.id


    def get_trip(self):
        return self.list_trip
    

    def get_list_neighbor(self):
        return self.list_neighbor

    def get_neighbor_by_rank(self, rank, mask):
        while rank < len(self.list_neighbor) - 1:
            index_target, distance = self.list_neighbor[rank]
            if index_target != -1:
                if mask[index_target] == 0:
                    return [index_target, distance]
            if rank > 0:   
                rank += 1
            if rank < 0:
                rank -= 1
