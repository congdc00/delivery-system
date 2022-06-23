import csv
import glob
import os
import matplotlib.pyplot as plt



def extract_info(path):

    dict_param = {
        "num_truck": 2,
        "cap_truck": 1500,
        "num_drone": 2,
        "cap_drone" :40,
        "duration_drone" : 30,
        "speed_drone": 0.6,
        "speed_truck": 0.4,
        "working_time": 60,
        }

    list_param = []
    list_target = []

    # đọc tên của file
    list_path = path.split("\\")
    name = list_path[3]
    list_tmp = name.split('.')

    # đọc các thông tin về tham số đầu vào
    for param in list_tmp:
        if param != 'csv':
            list_param.append(param)



    # đọc dữ liệu trong file
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        #read info target
        for row in csv_reader:
            if line_count != 0:

                list_tmp = []
                for i in range (0,6):
                    if i == 1 or i == 2:
                        list_tmp.append(float(row[i]))
                    else:
                        list_tmp.append(int(row[i]))
                list_target.append(list_tmp)

            line_count += 1

        return dict_param, list_target

def get_all_path(root_path):

    '''
    Load toàn bộ dữ liệu từ các file csv
    input: root_path file chứa data
    output: list path
    '''

    # Tìm tất cả các path csv
    list_path = glob.glob(os.path.join(root_path, "*.csv"))

    return list_path

def showHistogram(list_target):

    list_cordinate = []

    for target in list_target:
        list_cordinate.append([target[1],target[2]])

    '''
    input: coordinates (x,y)
    output: map of point
    '''
    x=[]
    y=[]

    #depot
    x.append(0)
    y.append(0)

    for target in list_cordinate:
        x.append(target[0])
        y.append(target[1])

    plt.title("Cordinate")

    plt.xlabel("Value X")

    plt.ylabel("Value Y")

    plt.plot(x, y, "go")

    plt.show()

def load_data(root_path):
    '''
    Lấy toàn bộ tham số của bài toán
    '''

    list_path = get_all_path(root_path)
    
    dict_param,list_target = extract_info(list_path[64])

    return dict_param, list_target