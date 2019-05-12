import pymysql.cursors

# Подключиться к базе данных.
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='mydb',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:

    with connection.cursor() as cursor:

        # SQL
        sql = "SELECT * FROM Classes"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Закрыть соединение (Close connection).
    connection.close()
    print("connect close")

