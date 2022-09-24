from readline import insert_text
import psycopg2 

HOSTNAME = "localhost"
DATABASE = 'delivery_system'
USERNAME = "postgres"
PWD = "Dinhchicong123."
PORT_ID = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = HOSTNAME,
        dbname = DATABASE,
        user = USERNAME,
        password = PWD,
        port = PORT_ID

    )
    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS list_customer (
                            id              int PRIMARY KEY,
                            id_order        int,
                            fullname        varchar(40),
                            phone_number    varchar(40),
                            age             int,
                            level_customer  int,
                            coordinate_x      varchar(40),
                            coordinate_y      varchar(40))'''
    cur.execute(create_script)

    insert_script = ''' INSERT INTO list_customer (id, id_order, fullname, phone_number, age, level_customer, coordinate_x, coordinate_y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
    insert_value = [(1, 2, "dinh chi cong", "0866080755", 22, 0, "20.9796604", "105.8887476"), (2, 3, "le minh hue", "0866080765", 15, 1, "20.9796604", "105.8887476")]
    for record in insert_value:
        cur.execute(insert_script, record)

    conn.commit()
    
except Exception as error:
    print(f"ket noi khong thanh cong {error}")

finally:
    if cur is not None:
        cur.close()
    
    if conn is not None:
        conn.close()
