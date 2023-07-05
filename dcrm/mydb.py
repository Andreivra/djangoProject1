import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Romania1986'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmdb")
