import mysql.connector
def fetchEmployee(cursor):
    cursor.execute("SELECT * FROM employees") 
    return list(cursor)

def main():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='anant',
            database='db1'
        )
        if mydb.is_connected():
            print("Connected to MySQL..")
            cursor = mydb.cursor()
            employeeList = fetchEmployee(cursor)

            for x in employeeList:
                print(x)
        else:
            print("Connection Failed..")
    except mysql.connector.Error as e:
        print("Error:", e)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

if __name__ == '__main__':
    main()
