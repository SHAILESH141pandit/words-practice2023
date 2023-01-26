import psycopg2
from DBpassword import pwd

database =  'postgres'
hostname = 'localhost'
port_id = '5432'
username = 'postgres'
# pwd = ''                  # Please! Enter postgres Data-base password.

conn, cur = None, None

def conectDB():
    try :
        conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id
                    )
        cur = conn.cursor()
        
        cur.execute('DROP TABLE IF EXISTS Word_List')


        create_script = '''
                    CREATE TABLE IF NOT EXISTS Word_List(
                        word str PRIMARY KEY,
                        meaning_of_word varchar(100) NOT NULL
                        )'''
        cur.execute(create_script)





        insert_script = 'INSERT INTO Word_List(word, meaning_of_word) VALUES(%s, %s)'
        insert_value = ("hello", 'hello')

        cur.execute(insert_script, insert_value)

        # insert_values = [(2, 'mohit', 1500, 'D2'), (3, 'raju', 2000, 'D1'), (4, 'alok', 8000, 'D4'), (5, 'amit', 5000, 'D3')]
        
        # for record in insert_values :
        #     cur.execute(insert_script, record)

        cur.execute('SELECT * FROM Word_List')
        # print(cur.fetchall())

        for record in cur.fetchall() :
            # print(record)
            print(record[1], record[2])





        conn.commit()
    except Exception as error :
        print(error)
    finally :
        if cur is not None :
            cur.close()
        if conn is not None :
            conn.close()