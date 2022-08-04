import psycopg2

import os

# DATABASE_URL = os.environ['DATABASE_URL']

localhost = "192.168.22.38"
""" insert a new vendor into the vendors table """
py_id = None
sql = """INSERT INTO tb_z1_player(py_name, shirt_number ) VALUES(%s, %s) RETURNING py_id"""
con = None
# connect to the database
try:
    con = psycopg2.connect(host = 'localhost',database = "postgres", user = "mario", password = "admin",)
    # con = psycopg2.connect(host = "192.168.22.12",database = "postgres", user = "postgres", password = "1234",)
    print('connected to database\n')
#cursor
except Exception as err:
    print(err)
    print('error connecting to database\n')
    exit()

try:
    cur = con.cursor()
    #execute a query

    cur.execute("select py_id from tb_z1_player")
    print(sql, 'sql ::: ')

    num_rows = cur.fetchall()
    gen_py_id =  num_rows[-1][0] + 1
    print(gen_py_id, 'gen_py_id ::: ')

    cur.execute(sql, ('mario',42,))
    py_id = cur.fetchone()[0]
    print(py_id,'py_id ::: ')

    con.commit()
    print("Records inserted........")

except Exception as err:
    print(err)
    print('error executing query\n')
    exit()

cur.close()
#close the connection
con.close()