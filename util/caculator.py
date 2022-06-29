
import sys

sys.path.append('/home/congdc/project/scheduled-delivery')
import math
from config import COORDINATES_DEPOT

def get_distant(cor_start, cor_end):
    x_start = cor_start[0]
    y_start = cor_start[1]
    x_end = cor_end[0]
    y_end = cor_end[1]

    distant = math.sqrt((x_start-x_end)**2 + (y_start-y_end)**2)

    return distant
def get_time(speed, cor_start, cor_end):
    distant = get_distant(cor_start, cor_end)
    time = distant/speed
    return time
def build_matrix_distant(list_target):

    '''
    Xay dung ma tran khoang cach tu du lieu dau vao
    '''

    matrix_distant = []


    for i in range (0,len(list_target) +1):
        if i == 0:
            cor_start = COORDINATES_DEPOT
        else:
            target_start = list_target[i-1]
            cor_start = target_start.get_cordinate()
        list_distant = []

        cor_end = COORDINATES_DEPOT
        distant = get_distant(cor_start, cor_end)
        list_distant.append(distant)

        # tinh khoan cach tu diem do toi tat ca cac diem con lai
        for target_end in list_target:
            cor_end = target_end.get_cordinate()

            distant = get_distant(cor_start, cor_end)

            list_distant.append(distant)
        
        matrix_distant.append(list_distant)

    return matrix_distant

def find_nearest_point(matrix_distant, index_target_start, list_index_target_end):
    '''
    Hàm tìm điểm gần nhất với index start cho trước
    OUTPUT: result la so cua diem gan nhat trong list_index_target_end [1,..20]
    result_index la index cua diem gan nhat trong list_index_target_end [1,..20]
    '''
    min_distant = float("Inf")
    result = 0
    index_target_in_list_index = -1
    for index_target_end in list_index_target_end:
        index_target_in_list_index += 1
        if matrix_distant[index_target_start][index_target_end] < min_distant:
            min_distant = matrix_distant[index_target_start][index_target_end]
            result = index_target_end
            result_index = index_target_in_list_index
        
    
    return result, result_index

    
