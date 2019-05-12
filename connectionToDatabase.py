import pymysql.cursors


def addClass_classEditor(line):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Classes'
            cursor.execute(sql)
            rows = cursor.fetchall()

            last = 0

            for row in rows:
                if row["idClasses"] > last:
                    last = row["idClasses"]
                if line == row["Class"]:
                    return False

            # SQL
            sql = 'select count(*) from Classes'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchone()
            sql = "insert into Classes (idClasses,Class) Values (" + str(last + 1) + ",'" + str(line) + "')"
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def showAllClasses_classEditor():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Classes'
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows



    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteClass_classEditor(line):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:

            # SQL
            sql = 'select * from Classes'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            idToDelete = -1;
            for row in rows:
                if row["Class"] == line:
                    idToDelete = row["idClasses"]
            sql = "delete from Classes where idClasses=" + str(idToDelete)
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# -----------------------------------------------------------

def addFeature_featureEditor(line):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Feature'
            cursor.execute(sql)
            rows = cursor.fetchall()

            last = 0

            for row in rows:
                if row["idFeature"] > last:
                    last = row["idFeature"]
                if line == row["NameFeature"]:
                    return False

            # SQL
            sql = 'select count(*) from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchone()
            sql = "insert into Feature (idFeature,nameFeature) Values (" + str(rows["count(*)"] + 1) + ",'" + str(
                line) + "')"
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def showAllFeatures():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Feature'
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteFeature_featureEditor(line):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:

            # SQL
            sql = 'select * from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            idToDelete = -1;
            for row in rows:
                if row["NameFeature"] == line:
                    idToDelete = row["idFeature"]
            sql = "delete from Feature where idFeature=" + str(idToDelete)
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# -----------------------------------------------------------

def setTypeOfFeature(line, type):
    type_to_add = -1
    if type == 'Scalar':
        type_to_add = 1
    if type == 'Logical':
        type_to_add = 2
    if type == 'Dimensional':
        type_to_add = 3

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:

            # SQL
            sql = 'select * from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            idToSetType = -1;
            for row in rows:
                if row["NameFeature"] == line:
                    idToSetType = row["idFeature"]

            sql = "update Feature set Type = " + str(type_to_add) + " where idFeature=" + str(idToSetType)
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def getTypeAlreadySelect(line):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:

            # SQL
            sql = 'select * from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            idToSetType = -1;
            for row in rows:
                if row["NameFeature"] == line:
                    if row["Type"] == 1:
                        return 'Scalar'
                    if row["Type"] == 2:
                        return 'Logical'
                    if row["Type"] == 3:
                        return 'Dimensional'
                    return "None"
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# ------------------------------------------------------------

def addScalarFeatureDef(featureName, line):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            # SQL
            sqlForeignKey = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKey)
            foreignKey = cursor.fetchone()["idFeature"]

            # SQL
            sql = "select * from ScalarValues where Feature_idFeature = " + str(foreignKey)
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                if row["Value"] == line:
                    return False

            # SQL
            sql = 'select count(*) from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchone()

            sql = "insert into ScalarValues (Feature_idFeature,Value) Values (" + \
                  "(" + sqlForeignKey + "),'" + line + "')"
            cursor.execute(sql)
            connection.commit()

        return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def showAllScalarFeatureDef(featureName):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            # SQL
            sqlForeignKey = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKey)
            foreignKey = cursor.fetchone()["idFeature"]

            # SQL
            sql = "select * from ScalarValues where Feature_idFeature = " + str(foreignKey)
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows


    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteScalarFeatureDef(featureName, line):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:

            sqlForeignKey = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKey)
            foreignKey = cursor.fetchone()["idFeature"]

            # SQL
            sql = "select * from ScalarValues where Feature_idFeature = " + str(foreignKey)
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchall()
            idToDelete = -1;
            for row in rows:
                if row["Value"] == line:
                    idToDelete = row["idScalarValues"]
            sql = "delete from ScalarValues where idScalarValues=" + str(idToDelete)
            cursor.execute(sql)
            connection.commit()
            return True

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# -----------------------------------------------------------

# IT ALSO DELETE PREVIOUS ROWS FOR THIS FEATURE!!!
def addLogicalFeatureDef(featureName, lineTrue, lineFalse):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            # SQL
            sqlForeignKey = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKey)
            foreignKey = cursor.fetchone()["idFeature"]

            # SQL
            sql = "delete from LogicalValues where Feature_idFeature = " + str(foreignKey)
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)

            sql = "insert into LogicalValues (Feature_idFeature,True_Value,False_Value) Values (" + \
                  "(" + sqlForeignKey + "),'" + lineTrue + "','" + lineFalse + "')"
            cursor.execute(sql)

            connection.commit()



    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# -----------------------------------------------------------
def addDimensionalFeatureDef(featureName, left, right, ifLeftIncluded=False, ifRightIncluded=False):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")

    if ifRightIncluded:
        ifRightIncluded = 1
    else:
        ifRightIncluded = 0

    if ifLeftIncluded:
        ifLeftIncluded = 1
    else:
        ifLeftIncluded = 0

    try:
        with connection.cursor() as cursor:
            # SQL
            sqlForeignKey = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKey)
            foreignKey = cursor.fetchone()["idFeature"]

            # SQL
            sql = "delete from DimensionalValues where Feature_idFeature = " + str(foreignKey)
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)

            sql = "insert into DimensionalValues (Feature_idFeature,LeftValueIncluded, LeftValue," \
                  "RightValueIncluded, RightValue) Values (" + \
                  "(" + sqlForeignKey + "),'" + str(ifLeftIncluded) + "','" + str(left).replace(',', '.') + "','" \
                  + str(ifRightIncluded) + "','" + str(right).replace(',', '.') + "')"
            cursor.execute(sql)

            connection.commit()



    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")
