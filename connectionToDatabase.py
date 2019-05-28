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


def getClassIdFromClassName(className):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select idClasses from Classes where Class = "' + className + '"'
            cursor.execute(sql)
            rows = cursor.fetchone()
            return rows["idClasses"]

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def showAllClasses():
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
                if row["idFeature"] >= last:
                    last = row["idFeature"]
                if line == row["NameFeature"]:
                    return False

            # SQL
            sql = 'select count(*) from Feature'
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            rows = cursor.fetchone()
            sql = "insert into Feature (idFeature,nameFeature) Values (" + str(last + 1) + ",'" + str(
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


def getFeatureIdByFeatureName(feature):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select idFeature from Feature where NameFeature = "' + feature + '"'
            cursor.execute(sql)
            rows = cursor.fetchone()
            return rows["idFeature"]

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

# IT ALSO DELETE PREVIOUS ROWS FOR THIS FEATURE!!!
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


# -----------------------------------------------------------

def addFeatureToClass_classExplanation(featureName, className):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")

    try:
        with connection.cursor() as cursor:

            sql = 'select * from Feature_Class_pair'
            cursor.execute(sql)
            rows = cursor.fetchall()

            last = 0

            for row in rows:
                if row["idFeature_Class_pair"] > last:
                    last = row["idFeature_Class_pair"]

            # SQL
            sqlForeignKeyFeature = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            # cursor.execute(sqlForeignKeyFeature)

            # SQL
            sqlForeignKeyClass = "select idClasses from Classes where Class = '" + className + "'"
            # cursor.execute(sqlForeignKeyClass)

            sql = "insert into Feature_Class_pair (idFeature_Class_pair,Classes_idClasses, Feature_idFeature)" \
                  " Values (" + str(last + 1) + ",(" + sqlForeignKeyClass + "),(" + sqlForeignKeyFeature + "))"
            cursor.execute(sql)

            connection.commit()



    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteFeatureFromClass_classExplanation(featureName, className):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")

    try:
        with connection.cursor() as cursor:

            # SQL
            sqlForeignKeyFeature = "select idFeature from Feature where NameFeature = '" + featureName + "'"
            cursor.execute(sqlForeignKeyFeature)
            feature = cursor.fetchone()
            # SQL
            sqlForeignKeyClass = "select idClasses from Classes where Class = '" + className + "'"
            cursor.execute(sqlForeignKeyClass)
            classId = cursor.fetchone()

            sqlPair = "select idFeature_Class_pair from Feature_Class_pair where " \
                      "Classes_idClasses = " + str(classId["idClasses"]) + \
                      " AND Feature_idFeature = " + str(feature["idFeature"])
            cursor.execute(sqlPair)
            pair = cursor.fetchone()
            sql = "delete from Feature_Class_pair where idFeature_Class_pair=" + str(pair["idFeature_Class_pair"])

            cursor.execute(sql)

            connection.commit()



    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def takeFeautureFromClass_classExplanation(className):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")

    try:
        with connection.cursor() as cursor:

            # SQL
            sqlForeignKeyClass = "select idClasses from Classes where Class = '" + className + "'"
            # cursor.execute(sqlForeignKeyClass)

            sql = "Select Feature_idFeature From Feature_Class_pair where Classes_idClasses = (" + sqlForeignKeyClass + ")"
            cursor.execute(sql)
            features = cursor.fetchall()

            result = []

            for row in features:
                sql = "Select * from Feature where idFeature = " + str(row["Feature_idFeature"])
                cursor.execute(sql)
                result.append(cursor.fetchone())

            return result




    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def showAllFeatures_classExplanation():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Feature where Type is not null'
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# ------------------------------------------------------------------

def takeTypeOfFeature(feature):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select Type from Feature where NameFeature = "' + feature + '"'
            cursor.execute(sql)
            row = cursor.fetchone()
            return row

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def getidFeatureClass_pairByIdClassIdFeature(idClass, idFeature):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = 'select idFeature_Class_pair from Feature_Class_pair where Feature_idFeature = ' + str(idFeature) + \
                  ' and Classes_idClasses = ' + str(idClass)
            cursor.execute(sql)
            row = cursor.fetchone()
            return row["idFeature_Class_pair"]

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def getIdFeatureClass_pairByClassNameFeatureName(featureName, className):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            idClass = getClassIdFromClassName(className)
            idFeature = getFeatureIdByFeatureName(featureName)
            featureClassPair = getidFeatureClass_pairByIdClassIdFeature(idClass, idFeature)
            return featureClassPair

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def setScalar_FeatureClass_pair(scalar, idFeatureClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "insert into ClassScalarlValue (Feature_Class_pair_idFeature_Class_pair,Value) " \
                  "Values ((" + str(idFeatureClass) + '),"' + str(scalar) + '")'
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteScalar_FeatureClass_pair(idFeatureClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "delete from ClassScalarlValue where Feature_Class_pair_idFeature_Class_pair=" + str(idFeatureClass)
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteLogical_FeatureClass_pair(idFeatureClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "delete from ClassLogicalValue where Feature_Class_pair_idFeature_Class_pair=" + str(idFeatureClass)
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def getLogicalTrueFalse_FeatureClass_pair(featureId):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "Select * from LogicalValues where Feature_idFeature = " + str(featureId)
            cursor.execute(sql)
            row = cursor.fetchone()
            return list(row["True_Value"] + row["False_Value"])

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def setLogicalTrueFalse_FeatureClass_pair(idFeatureClass, trueValue, falseValue):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            if trueValue and not falseValue:
                sql = "insert into ClassLogicalValue (Feature_Class_pair_idFeature_Class_pair,True_Value) " \
                      "Values ((" + str(idFeatureClass) + '),"' + str(trueValue) + '")'
            if not trueValue and falseValue:
                sql = "insert into ClassLogicalValue (Feature_Class_pair_idFeature_Class_pair,False_Value) " \
                      "Values ((" + str(idFeatureClass) + '),"' + str(falseValue) + '")'
            if trueValue and falseValue:
                sql = "insert into ClassLogicalValue (Feature_Class_pair_idFeature_Class_pair,True_Value,False_Value) " \
                      "Values ((" + str(idFeatureClass) + '),"' + str(trueValue) + '","' + str(falseValue) + '")'

            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def getDimensionalValueMinMax_FeatureClass_pair(featureId):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "Select * from DimensionalValues where Feature_idFeature = " + str(featureId)
            cursor.execute(sql)
            row = cursor.fetchone()
            left = row["LeftValue"]
            right = row["RightValue"]
            if row["LeftValueIncluded"] == 0:
                left = left + 0.001
            if row["RightValueIncluded"] == 0:
                right = right - 0.001
            result = []
            result.append(left)
            result.append(right)
            return result

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def deleteDimensionalValue_FeatureClass_pair(idFeatureClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "delete from ClassDimensionalValue where Feature_Class_pair_idFeature_Class_pair=" + str(
                idFeatureClass)
            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def setDimensionalValue_FeatureClass_pair(idFeatureClass, minValue, maxValue):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "insert into ClassDimensionalValue (Feature_Class_pair_idFeature_Class_pair,LeftValue,RightValue) " \
                  "Values ((" + str(idFeatureClass) + '),' + str(minValue).replace(',', '.') + ',' + str(
                maxValue).replace(',', '.') + ')'

            cursor.execute(sql)
            connection.commit()

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


def isSet(idFeatureClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "select * from ClassDimensionalValue where Feature_Class_pair_idFeature_Class_pair =" + str(
                idFeatureClass)
            cursor.execute(sql)
            row1 = cursor.fetchall()
            sql = "select * from ClassLogicalValue where Feature_Class_pair_idFeature_Class_pair =" + str(
                idFeatureClass)
            cursor.execute(sql)
            row2 = cursor.fetchall()
            sql = "select * from ClassScalarlValue where Feature_Class_pair_idFeature_Class_pair =" + str(
                idFeatureClass)
            cursor.execute(sql)
            row3 = cursor.fetchall()

            return len(row1) > 0 or len(row2) > 0 or len(row3) > 0


    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")


# --------------------DETECT CLASS------------------
def getAllClassFeature_pair():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "Select * from Feature_Class_pair"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")

def getFeatureById(idFeature):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "Select * from Feature where idFeature ="+str(idFeature)
            cursor.execute(sql)
            rows = cursor.fetchone()
            return rows

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")

def getClassById(idClass):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mydb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connection established")
    try:
        with connection.cursor() as cursor:
            sql = "Select * from Classes where idClasses ="+str(idClass)
            cursor.execute(sql)
            rows = cursor.fetchone()
            return rows

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        # Закрыть соединение (Close connection).
        connection.close()
        print("connect close")
