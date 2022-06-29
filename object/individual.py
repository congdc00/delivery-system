class Individual():
    def __init__(self,id, list_trip_drone, list_trip_truck, list_target):
        self.id = id
        self.fitness = 0
        self.point = 0
        self.list_trip_drone = list_trip_drone
        self.list_trip_truck = list_trip_truck
        self.list_target = list_target

    def update_fitness(self, fitness):
        self.fitness = fitness

    def update_point(self, point):
        self.point = point

    def get_fitness(self):
        return self.fitness
    
    def get_point(self):
        return self.point

    def get_info_target(self):
        return self.list_target 