from readline import insert_text
import psycopg2 
import psycopg2.extras

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
    cur = conn.cursor(
        cursor_factory=psycopg2.extras.DictCursor
    )

    select_scrip = 'SELECT * FROM list_order'
    cur.execute(select_scrip)
    result = cur.fetchall()
    for text in result:
        print(text['id'], text['time_order'])

    

    conn.commit()
    
except Exception as error:
    print(f"ket noi khong thanh cong {error}")

finally:
    if cur is not None:
        cur.close()
    
    if conn is not None:
        conn.close()