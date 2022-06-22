import math

def find_nearest_point(cor_start,list_target):
    '''
    Hàm tìm điểm gần nhất với index start cho trước
    input:  cor_start [x,y]
            list_target Danh sách target như đầu vào
    '''
    x_start = cor_start[0]
    y_start = cor_start[1]
    min_distant = math.inf
    index_best_point = -1

    for index,x_end, y_end,_,_,_ in list_target:
        distant = math.sqrt((x_start-x_end)**2 + (y_start-y_end)**2)
        print("khoang cach vi tri {} la {}".format(index, distant))
        if distant < min_distant:
            min_distant = distant
            index_best_point = index

    return index_best_point