import mysql.connector

def readBLOB():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='your database',
                                             user='your username',
                                             password='your password',auth_plugin='mysql_native_password')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from table"""

        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            print("Name = ", row[0])
            file1 = row[1].decode('utf-8')
            print(file1)
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")    

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

readBLOB()    
        
