import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from calculator.fitness_and_point import get_fitness_and_point
class Individual():
    def __init__(self,id, list_drone, list_truck, list_target):
        self.id = id
        self.list_drone = list_drone
        self.list_truck = list_truck
        self.list_target = list_target
        self.point, self.fitness = get_fitness_and_point(list_target)

    def update_fitness(self, fitness):
        self.fitness = fitness

    def update_point(self, point):
        self.point = point

    def update_individual(self,list_drone,list_truck, list_target):
        self.list_drone = list_drone
        self.list_truck = list_truck
        self.list_target = list_target
        self.point, self.fitness = get_fitness_and_point(list_target)
    
    def update_target(self,target, index):
        self.list_target[index] = target
        self.point, self.fitness = get_fitness_and_point(self.list_target)

    def get_id(self):
        return self.id

    def get_fitness(self):
        return self.fitness
    
    def get_point(self):
        return self.point

    def get_list_target(self):
        return self.list_target 
    
    def get_list_drone(self):
        return self.list_drone

    def get_list_truck(self):
        return self.list_truck