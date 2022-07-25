class Turn:
    def __init__(self, id_target, id_device, bound):
        self.id_target = id_target
        self.id_device = id_device
        self.bound = bound

    def update_target(self, new_id_target):
        self.id_target = new_id_target
    
    def update_device(self, new_id_device):
        self.id_device = new_id_device

    def update_bound(self, new_bound):
        self.bound = new_bound

    def get_target(self):
        return self.id_target

    def get_device(self):
        return self.id_device

    def get_bound(self):
        return self.bound

    
