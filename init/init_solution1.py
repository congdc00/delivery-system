
import sys

sys.path.append('/home/congdc/project/scheduled-delivery')

from util.read_data import load_list_device, load_list_target
from util.caculator import find_nearest_point,find_furthest_point, build_matrix_distant, get_time
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


def create_trip(device, matrix_distant, list_index_target_wait, list_index_target_done, list_target, type):
    '''
    INPUT: list_target: danh sách target khởi tạo ban đầu
    OUTPUT: 
    '''
    new_trip =[]

    cor_start = COORDINATES_DEPOT
    if type == "drone":
        index_end, index_pop = find_nearest_point(matrix_distant, 0, list_index_target_wait)
    else:
        index_end, index_pop = find_furthest_point(matrix_distant, 0, list_index_target_wait)

    id_target = index_end - 1
    cor_end = list_target[id_target].get_cordinate()

    
    while check_condition(device, cor_start, cor_end, type = type):
        print("+ them hang")
        target = list_target[id_target]

        # neu lower bound bang 0 thi co gang giao 
        lower_bound,uper_bound = target.get_bound()
        weight_drone = device.get_capacity()
        if type != "drone" or lower_bound == 0:
            if weight_drone <= uper_bound:
                weight_package = weight_drone
            else:
                weight_package = uper_bound
                list_index_target_done.append(list_index_target_wait.pop(index_pop))
                print("danh sach khach hang con lai: {}".format(list_index_target_wait))
        else:
            if weight_drone <= lower_bound:
                weight_package = weight_drone
            else:
                weight_package = lower_bound
                list_index_target_done.append(list_index_target_wait.pop(index_pop))
                print("danh sach khach hang con lai: {}".format(list_index_target_wait))
            
            
            


        # tinh thoi gian can di 
        speed_drone = device.get_speed()
        time = get_time(speed_drone, cor_start, cor_end)

        # cap nhap gia tri cho drone
        device.update_time(time)
        device.update_capacity(weight_package)

        # cap nhap gia tri cho target
        list_target[id_target].update_bound(weight_package, type = 1)
        list_target[id_target].add_trip([device.get_id(), weight_package])
        
        print("giao them hang {}".format([id_target, weight_package]))
        print("target bound {}".format(list_target[id_target].get_bound()))
        print("trong luong con lai cua device: {}".format(device.get_capacity()))

        if type == "drone":
            print("thoi gian nhiem vu con lai cua device: {}".format(device.get_duration()))

        print("thoi gian con lai toan nhiem vu: {}".format(device.get_working_time()))
        new_trip.append([id_target, weight_package])

        #chuyen sang diem tiep theo
        if len(list_index_target_wait) == 0:
            break

        cor_start = cor_end
        index_end, index_pop = find_nearest_point(matrix_distant, index_end, list_index_target_wait)
        id_target = index_end - 1
        cor_end = list_target[id_target].get_cordinate()

    return new_trip, device, list_index_target_wait, list_index_target_done, list_target

def schedule_drone(list_drone, matrix_distant, list_index_target_wait, list_target):

    '''
    Hàm lập lịch di chuyển cho drone
    input: danh sách các drone khả dụng, danh sách các target chưa giao
    output: Danh sách lịch trình di chuyển của drone
    '''

    list_trip_drone = []
    list_index_target_done = []
    list_drone_available = list (range(0, len(list_drone), 1 ))
    index_trip = -1

    # Neu van con thiet bi de giao
    while len(list_drone_available) > 0 and len(list_index_target_wait) > 0:
        index_trip += 1
        index = 0
        while index < len(list_drone_available):
            
            i = list_drone_available[index]
            # Tao dong cho chinh thiet bi drone do
            if index_trip == 0:
                list_trip_drone.append([])

            # tao trip moi cho drone
            old_time = list_drone[i].get_working_time()
            print("-------Tao trip cho drone {} ------------".format(list_drone[i].get_id()))
            new_trip, list_drone[i], list_index_target_wait, list_index_target_done, list_target = create_trip(list_drone[i], matrix_distant, list_index_target_wait, list_index_target_done, list_target, type ="drone")
            
            #quay ve kho va reset lai suc chua va thoi gian
            list_drone[i].reset_capacity()
            list_drone[i].reset_duration()
            new_time = list_drone[i].get_working_time()


            # Neu drone khong di chuyen => pop
            if new_time == old_time:
                print("!!! drone bi loai {}".format(list_drone_available[index]))
                list_drone_available.pop(index)
                index -= 1
            else:
                id = list_drone[i].get_id()
                list_trip_drone[id].append(new_trip)

            #neu het target de giao => ket thuc
            if len(list_index_target_wait) == 0:
                break
                
            index += 1
            

    return list_trip_drone, list_index_target_wait, list_index_target_done, list_target


def schedule_truck(list_truck, matrix_distant, list_index_target_wait,list_index_target_done, list_target):
    list_trip_truck = []

    for i in range (0, len(list_truck)):
        new_trip, list_truck[i], list_index_target_wait, list_index_target_done, list_target = create_trip(list_truck[i], matrix_distant, list_index_target_wait, list_index_target_done, list_target, type="truck")
        list_trip_truck.append(new_trip)
        if len(list_index_target_wait) == 0:
            break

    return list_trip_truck, list_index_target_wait, list_index_target_done, list_target
if __name__ == "__main__":

    # Load tập object target, drone, truck
    list_target = load_list_target(ROOT_PATH_DATA)
    #showHistogram(list_target)
    list_drone, list_truck = load_list_device()

    # xay dung ma tran khoang cach
    matrix_distant = build_matrix_distant(list_target)


    # khoi tao hang doi target
    num_target = len(list_target)
    list_index_target_wait = list ( range ( 1, num_target+1, 1 ))
    print ("Diem xa nhat: {}".format(find_furthest_point(matrix_distant, 0, list_index_target_wait)))

    # Lập lịch cho các drone
    list_trip_drone, list_index_target_wait,list_index_target_done, list_target = schedule_drone(list_drone, matrix_distant, list_index_target_wait, list_target)


    print("-------------------ket thuc qua trinh giao hang cua drone ------------------------------")
    print(list_trip_drone)
    print ("danh sach target còn lại: {}".format(list_index_target_wait))
    print ("danh sach target giao xong : {}".format(list_index_target_done))
    print("-------------------khoi dong giao hang bang truck----------------------------------------")
    
    list_trip_truck, list_index_target_wait,list_index_target_done, list_target = schedule_truck(list_truck, matrix_distant, list_index_target_wait,list_index_target_done, list_target)

    print("-------------------ket thuc qua trinh giao hang cua truck ------------------------------")
    print(list_trip_truck)
    print ("danh sach target còn lại: {}".format(list_index_target_wait))
    print ("danh sach target giao xong : {}".format(list_index_target_done))
    
    print("------------danh sach target---------------")
    for target in list_target:
        print("id_target: {}".format(target.get_id()))
        print("trip fo target {}".format(target.get_trip()))
    print("--------------------------done----------------------------------------")