import math

def get_distant(cor_start, cor_end):
    x_start = cor_start[0]
    y_start = cor_start[1]
    x_end = cor_end[0]
    y_end = cor_end[1]

    distant = math.sqrt((x_start-x_end)**2 + (y_start-y_end)**2)

    return distant

def find_nearest_point(cor_start,list_target):
    '''
    Hàm tìm điểm gần nhất với index start cho trước
    input:  cor_start [x,y]
            list_target Danh sách target như đầu vào
    '''
    min_distant = math.inf

    index = -1
    for _,x_end, y_end,_,_,_ in list_target:
        index += 1
        cor_end = [x_end, y_end]
        #
        distant = get_distant(cor_start, cor_end)
        if distant < min_distant:
            min_distant = distant
            index_best_point = index
    print("best target la {}".format(index_best_point))
    print("so luong target {}".format(index))
    return index_best_point, min_distant