import psycopg2
import random

import os

# DATABASE_URL = os.environ['DATABASE_URL']
class FootballClub():
    def __init__(self,):
        print(' __init__ ::: ')
    localhost = "192.168.22.38"
    py_id = None
    sql = """INSERT INTO tb_z1_player(py_name, shirt_number ) VALUES(%s, %s) RETURNING py_id"""
    con = None

    def InsertNewPlayer(self, py_name, shirt_number):
        try:
            con = psycopg2.connect(host = 'localhost',database = "postgres", user = "mario", password = "admin",)
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
            print(self.sql, 'sql ::: ')

            # num_rows = cur.fetchall()
            # gen_py_id =  num_rows[-1][0] + 1
            # print(gen_py_id, 'gen_py_id ::: ')

            cur.execute(self.sql, (py_name,shirt_number))
            py_id = cur.fetchone()[0]
            # print(py_id,'py_id ::: ')

            con.commit()
            print("Records inserted........",py_id,py_name,shirt_number)

        except Exception as err:
            print(err)
            print('error executing query\n')
            exit()
        finally:
            # closing database connection.
            if con:
                cur.close()
                con.close()
                print("PostgreSQL connection is closed")

    player_name = 'Mario'
    shirt_number = random.randint(0,150)
    # insertNewPlayer(player_name, shirt_number)

    def UpdatePlayer(self, py_id, py_name):
        try:
            try:
                con = psycopg2.connect(host = 'localhost',database = "postgres", user = "mario", password = "admin",)
                print('connected to database\n')
            #cursor
            except Exception as err:
                print(err)
                print('error connecting to database\n')
                exit()

            cur = con.cursor()
            #execute a query
            print("Table Before updating record ")
            sql_select_query = """select * from tb_z1_player where py_id = %s"""
            cur.execute(sql_select_query, (py_id,))
            record = cur.fetchone()
            print(record)

            # Update single record now
            sql_update_query = """Update tb_z1_player set py_name = %s where py_id = %s"""
            cur.execute(sql_update_query, (py_name, py_id))
            con.commit()
            count = cur.rowcount
            print(count, "Record Updated successfully ")
            
            con.commit()
            print("Records inserted........",py_id,py_name)

        except Exception as err:
            print(err)
            print('error executing query\n')
            exit()
        finally:
            # closing database connection.
            if con:
                cur.close()
                con.close()
                print("PostgreSQL connection is closed")

py_id = 55
player_name = input("Enter player name: ")
shirt_number = random.randint(0,150)
FootballClub().InsertNewPlayer(player_name, shirt_number)
