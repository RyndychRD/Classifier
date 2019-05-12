import pymysql.cursors


def addClass(line):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = 'select count(*) from Classes'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows=cursor.fetchall()

            for row in rows:
                print(row["count(*)"])
            sql = "insert into Classes (idClasses,Class) Values ("+\
                str(row["count(*)"])+",\'"+str(line)+ "\')"
            cursor.execute(sql)


    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")

