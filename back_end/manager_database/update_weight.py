import sys
sys.path.append('/Users/dinhchicong/Project/delivery-system/back_end')

import json

with open("/Users/dinhchicong/Project/delivery-system/server/data_tmp/customer01/info.json") as f:
    data = json.load(f)
    coordinate = data["info_customer"]["location"]["coordinate"]
    print(coordinate)


import psycopg2 