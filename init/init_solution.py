
import sys

sys.path.append('/home/congdc/project/scheduled-delivery')

from util.read_data import load_data
from util.caculator import find_nearest_point, get_distant
from config import ROOT_PATH_DATA, COORDINATES_DEPOT

def create_list_drone(num_drone):
    '''
    Tạo danh sách các thiết bị drone
    '''

    list_drone = list ( range ( 0, num_drone, 1 )) 
    return list_drone

def get_info_point_next(speed_drone, point_start, list_target_wait):
    '''
    Lấy các thông tin về điểm tới tiếp theo
    '''
    index_target, distant = find_nearest_point(point_start, list_target_wait)
    target = list_target_wait[index_target]

    x = target[1]
    y = target[2]
    cor_target = [x, y]

    time_forward = distant/speed_drone
    time_backward = get_distant(COORDINATES_DEPOT, cor_target) / speed_drone
    return index_target, time_forward, time_backward

def drop_package(limit_weigth, list_target, index_target):
    '''
    Hàm thực hiện chức năng thả gói hàng xuống
    '''
    lower_bound = list_target[index_target][3]

    if limit_weigth >= lower_bound:
        weight_package = lower_bound
        limit_weigth -= lower_bound
        list_target.pop(index_target)

    else:
        weight_package = limit_weigth
        lower_bound -= limit_weigth
        list_target[index_target][3] = lower_bound
        limit_weigth = 0

    return weight_package, limit_weigth, list_target

def check_drone_limit(info_drone_limit, time_forward, time_backward):

    if info_drone_limit[1] == 0:
        return False

    if info_drone_limit[2] - time_forward < time_backward:
        return False

    if info_drone_limit[3] - time_forward < time_backward:
        return False

    return True

def create_trip(info_drone_limit, list_target_wait):

    '''
    Hàm tạo ra đường đi trong 1 trip
    input: danh sách target chưa giao
    output: lịch trình giao các target như thế nào
    '''
    list_point = []
    speed_drone = info_drone_limit[0]

    # Xuất phát tại vị trí kho
    point_start = COORDINATES_DEPOT

    index_target, time_forward, time_backward = get_info_point_next(speed_drone, point_start, list_target_wait)
    i_target = list_target_wait[index_target][0]

    while check_drone_limit(info_drone_limit, time_forward, time_backward):

        #Di chuyển đến điểm cần giao
        info_drone_limit[2] -= time_forward
        info_drone_limit[3] -= time_forward
        point_start[0] = list_target_wait[index_target][1]
        point_start[1] = list_target_wait[index_target][2]


        #Thả gói hàng xuống 
        weight_package, new_weight, new_list_target = drop_package(info_drone_limit[1], list_target_wait, index_target)
        info_drone_limit[1] = new_weight

        list_target_wait = new_list_target

        # Lưu hành trình vào trip 
        list_point.append([i_target, weight_package])

        if len(list_target_wait) == 0:
            return list_point, info_drone_limit[3]

        # Tìm điểm gần nhất cho chuyến đi tiếp theo
        index_target, time_forward, time_backward = get_info_point_next(speed_drone, point_start, list_target_wait)

    return list_point, info_drone_limit[3]

def schedule_drone(list_drone, info_drone_limit , list_target_wait):

    '''
    Hàm lập lịch di chuyển cho drone
    input: danh sách các drone khả dụng, danh sách các target chưa giao
    output: Danh sách lịch trình di chuyển của drone
    '''

    list_trip_drone = []
    i_trip = -1
    working_time = []

    while len(list_drone) > 0 :
        i_trip += 1
        index = -1
        for i_drone in list_drone:
            if len(list_target_wait) == 0:
                break

            index += 1
            #Tạo mảng để lưu các trip của drone i

            if i_trip == 0:
                list_trip_drone.append([])
                working_time.append(info_drone_limit[3])
                print("Tạo trip mới")

            # Tạo trip mới
            info_drone = [info_drone_limit[0],info_drone_limit[1],info_drone_limit[2],working_time[index]]
            trip, new_working_time = create_trip(info_drone,list_target_wait)
            working_time[index] = new_working_time

            if len(trip) != 0:
      
                # Thêm trip vào hành trình của drone
                list_trip_drone[i_drone].append(trip)
                print("tạo thành công trip cho drone {}, thời gian còn lại {}".format(list_drone[index],working_time[index]))
            else:

                #Loại drone ra khỏi danh sách sẵn sàng
                print("tạo thất bại trip cho drone {}, thời gian còn lại {}".format(list_drone[index],working_time[index]))
                list_drone.pop(index)
                index -= 1
        if len(list_target_wait) == 0:
                break
    return list_trip_drone

if __name__ == "__main__":

    # load tập data lên
    dict_param, list_target = load_data(ROOT_PATH_DATA)
    list_target_wait = list_target

    # Khởi tạo tập drone
    list_drone = create_list_drone(dict_param['num_drone'])

    info_drone_limit = [ dict_param["speed_drone"], dict_param["cap_drone"], dict_param['duration_drone'],dict_param["working_time"]]


    # Lập lịch cho các drone
    list_trip_drone = schedule_drone(list_drone,info_drone_limit, list_target_wait)

    print(list_trip_drone)

    # Khởi tạo tập drone
    list_truck = create_list_drone(dict_param['num_truck'])

    # Lập lịch cho các drone
    list_trip_truck = schedule_drone(list_truck,info_drone_limit, list_target_wait) 
    