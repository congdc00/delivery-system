from until import read_data
from until.caculator import find_nearest_point
from config import ROOT_PATH_DATA

def create_list_drone(num_drone):
    list_drone = list ( range ( 0, num_drone, 1 )) 
    return list_drone

if __name__ == "__main__":

    # load tập data lên
    dict_param, list_target = load_data(ROOT_PATH_DATA)

    # Khởi tạo tập drone
    list_drone = create_list_drone(dict_param['num_drone'])

    print(list_drone)
    cor_depot = [0,0]

    index = find_nearest_point(cor_depot, list_target)

    print(index)