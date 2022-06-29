from re import X
from tkinter import Y


class Target():
    def __init__(self,id,x,y,lower_bound, upper_bound, weight):
        self.id =id
        self.x = x
        self.y = y 
        self.lower_bound = lower_bound
        self.lower_bound_base = lower_bound
        self.upper_bound = upper_bound
        self.upper_bound_base =upper_bound
        self.weight = weight
        self.list_trip = []
    
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

    def add_trip(self, new_component):
        self.list_trip.append(new_component)

    def get_bound(self):
        return self.lower_bound, self.upper_bound

    def get_cordinate(self):
        return [self.x, self.y]
    
    def get_id(self):
        return self.id
