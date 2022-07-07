
import sys
import copy
sys.path.append('/Users/dinhchicong/Project/scheduled-deliver')
import numpy as np
import csv
from util.load_data import load_list_device, load_list_target
from calculator.distant import get_time
from util.show_histogram import showHistogram
from config import ROOT_PATH_DATA, COORDINATES_DEPOT


def check_condition(device , cor_start, cor_end, type):
    speed = device.get_speed()
    if type == "drone":
        duration = device.get_duration()

    working_time = device.get_working_time()
    time_need = get_time(speed, cor_start, cor_end) + get_time(speed, cor_end, COORDINATES_DEPOT)

    if type == "drone":
        if time_need > duration:
            return False
        
    if time_need > working_time:
            return False

    
    weight = device.get_capacity()
    if weight == 0:
        return False
    
    return True
def check_available(mask_target_wait):
    for i in mask_target_wait:
        if i == 0:
            return True 
    
    return False

def create_trip(device, mask_target_wait, depot, list_target, type):
    '''
    INPUT: list_target: danh sách target khởi tạo ban đầu
    OUTPUT: 
    '''

    new_trip = []
    cd_start = COORDINATES_DEPOT
    
    if type == "drone":
        index_target_next,_ = depot.get_neighbor_by_rank(-1, mask_target_wait)
    else:
        index_target_next,_ = depot.get_neighbor_by_rank(1, mask_target_wait)

    cd_end = list_target[index_target_next].get_coordinate()

    
    while check_condition(device, cd_start, cd_end, type = type):


        target = list_target[index_target_next]
        lower_bound, upper_bound = target.get_bound()

        
        weight_drone = device.get_capacity()
        #print("trong luong cua drone con lai {}".format(weight_drone))
        if type != "drone" or lower_bound == 0:
            weight_package = min(upper_bound, weight_drone)
        else:
            weight_package = min(lower_bound, weight_drone)
            
            
            


        # Cap nhap gia tri cho drone
        speed_drone = device.get_speed()
        time = get_time(speed_drone, cd_start, cd_end)
        device.update_time(time)
        device.update_capacity(weight_package)
        new_trip.append([index_target_next, weight_package])
        #print("+ tha diem {} trong luong {}".format(index_target_next, weight_package))


        # cap nhap gia tri cho target
        target.update_bound(weight_package, type = 1)
        lower_bound, _ = target.get_bound()
        if lower_bound <= 0:
            mask_target_wait[index_target_next] = 1
        target.add_trip([device.get_id(), weight_package])
        list_target[index_target_next] = target
        
        # xem con diem nao co the di tiep khong
        if check_available(mask_target_wait) == False:
            break
        
        # Chuyen sang diem tiep theo
        cd_start = cd_end

        index_target_next, _ = target.get_neighbor_by_rank(1, mask_target_wait)
        cd_end = list_target[index_target_next].get_coordinate()
    #print("--------")
    #print("trip duoc them vao {}".format(new_trip))
    #print("--------")
    if len(new_trip) != 0:
        device.create_trip(new_trip)
    return device, mask_target_wait, list_target
    


def schedule_drone(list_drone, mask_target_wait, depot,list_target):

    '''
    Hàm lập lịch di chuyển cho drone
    input: danh sách các drone khả dụng, danh sách các target chưa giao
    output: Danh sách lịch trình di chuyển của drone
    '''

    mask_drone_available = [0]*len(list_drone)

    # Neu van con thiet bi de giao
    while check_available(mask_drone_available) and check_available(mask_target_wait):
        index = 0
        for index in range (0, len(list_drone)):
            if mask_drone_available[index] == 0:
                #print("Lap lich cho drone {}".format(index))
                drone = list_drone[index]

                # tao trip moi cho drone
                old_time = drone.get_working_time()
                drone, mask_target_wait, list_target = create_trip(drone, mask_target_wait, depot, list_target, type ="drone")
                new_time = drone.get_working_time()

                #quay ve kho va reset lai suc chua va thoi gian
                drone.reset_capacity()
                drone.reset_duration()
                
                list_drone[index] = drone
                #print("trip drone {} tao ra: {}".format(index, drone.get_list_trip()))
                # Neu drone khong di chuyen => pop
                if new_time == old_time:
                    mask_drone_available[index] = 1
                    
                #neu het target de giao => ket thuc
                if check_available(mask_target_wait) == False:
                    break

            

    return list_drone, mask_target_wait, list_target


def schedule_truck(list_truck, mask_target_wait,depot, list_target):

    for i in range (0, len(list_truck)):

        truck  = list_truck[i]
        truck, mask_target_wait, list_target = create_trip(truck, mask_target_wait,depot, list_target, type="truck")
        
        if check_available(mask_target_wait) == False:
            break

        list_truck[i] = truck

    return list_truck, mask_target_wait, list_target


def init_solution1(list_drone, list_truck,depot, list_target):       
    
    ''' Khoi tao init solution 1
    descript: drone di nhung diem gan nhat, truck di nhung diem xa nhat roi moi di cac diem gan diem do
    '''       

    # Tach dia chi bo nho doc lap voi bai toan
    new_list_drone = copy.deepcopy(list_drone)
    new_list_truck = copy.deepcopy(list_truck)
    new_list_target = copy.deepcopy(list_target)

    # khoi tao hang doi target
    num_target = len(list_target)
    mask_target_wait = [0]*num_target

    # Lap lich
    new_list_drone, mask_target_wait, new_list_target = schedule_drone(new_list_drone, mask_target_wait,depot, new_list_target)
    
    new_list_truck, mask_target_wait, new_list_target = schedule_truck(new_list_truck, mask_target_wait,depot, new_list_target)
    
    return new_list_drone, new_list_truck, new_list_target

if __name__ == "__main__":

    pass
