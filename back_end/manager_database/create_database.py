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

    cur.execute('DROP TABLE IF EXISTS list_order')

    create_script = ''' CREATE TABLE IF NOT EXISTS list_order (
                            id          int PRIMARY KEY,
                            type        varchar(40),
                            time_order  varchar(40),
                            weight      int)'''
    cur.execute(create_script)

    insert_script = ''' INSERT INTO list_order (id, type, time_order, weight) VALUES (%s, %s, %s, %s) '''
    insert_value = [(2, "express", "2022-09-09", 0), (3, "express", "2022-09-09", 0)]
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
