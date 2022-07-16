import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from calculator.fitness_and_point import get_fitness_and_point
class Individual():
    def __init__(self,id, list_device, list_target):
        self.id = id
        self.list_device = list_device
        self.list_target = list_target
        self.point, self.fitness = get_fitness_and_point(list_target, list_device)

    def update_fitness(self, fitness):
        self.fitness = fitness

    def update_point(self, point):
        self.point = point

    def update_individual(self,list_device, list_target):
        self.list_device = list_device
        self.list_target = list_target
        self.point, self.fitness = get_fitness_and_point(list_target, list_device)
    
    def update_target(self,target, index):
        self.list_target[index] = target
        self.point, self.fitness = get_fitness_and_point(self.list_target, self.list_device)

    def get_id(self):
        return self.id

    def get_fitness(self):
        return self.fitness
    
    def get_point(self):
        return self.point

    def get_list_target(self):
        return self.list_target 
    
    def get_list_device(self):
        return self.list_device
