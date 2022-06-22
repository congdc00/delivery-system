from until.read_data import load_data
from until.caculator import find_nearest_point
from config import ROOT_PATH_DATA


if __name__ == "__main__":

    # load tập data lên
    dict_param, list_target = load_data(ROOT_PATH_DATA)

    cor_depot = [0,0]

    index = find_nearest_point(cor_depot, list_target)

    print(index)