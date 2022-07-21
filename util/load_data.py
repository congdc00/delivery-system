import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

import csv
import glob
import os
from object.target import Target
from object.devices_drone import create_list_drone
from object.devices_truck import create_list_truck
from config import NUM_TRUCK, CAP_TRUCK, NUM_DRONE, CAP_DRONE, DURATION_DRONE, SPEED_DRONE, SPEED_TRUCK, WORKING_TIME



def extract_info_target(path):

    # đọc dữ liệu trong file
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        list_target = []
        #read info target
        for row in csv_reader:
            if line_count != 0:
                
                id = int(row[0])
                x = float(row[1])
                y = float(row[2])
                lower_bound = int(row[3])
                upper_bound = int(row[4])
                weight = int(row[5])
                target = Target(id, x, y, lower_bound, upper_bound, weight)
                list_target.append(target)
            line_count += 1

        return list_target

def extract_name(path):

    list_info = path.split("/")
    len_name = len(list_info) - 1
    name = list_info[len_name]

    return name

def get_all_path(root_path):

    '''
    Load toàn bộ dữ liệu từ các file csv
    input: root_path file chứa data
    output: list path
    '''

    # Tìm tất cả các path csv
    list_path = glob.glob(os.path.join(root_path, "*.csv"))
    dict_path = {}
    for path in list_path:
        name = extract_name(path)
        dict_path[name] = path

    return dict_path

def load_list_target(root_path):

    '''
    Lấy toàn bộ tham số của bài toán
    '''
    # File thuc hien
    name_file = '20.5.4.csv'
    # Lấy danh sách các path
    dict_path = get_all_path(root_path)
    
    list_target = extract_info_target(dict_path[name_file])

    return list_target 

def load_list_device():
    info_drone_base = [SPEED_DRONE, CAP_DRONE, DURATION_DRONE, WORKING_TIME]
    list_drone = create_list_drone(NUM_DRONE, info_drone_base)
    info_truck_base = [SPEED_TRUCK, CAP_TRUCK, WORKING_TIME]
    list_truck =  create_list_truck(NUM_TRUCK, info_truck_base)
    list_device = list_drone + list_truck
    
    return list_device 


#test
if __name__ == "__main__":
    type_test = 1
    if type_test == 0:
        list_target = load_list_target("/Users/dinhchicong/Project/scheduled-delivery/data/data_test")
        low, up = list_target[1].get_bound()
        print(up)
    elif type_test == 1:
        list_drone = load_list_device()
        print(list_drone[1].get_duration())