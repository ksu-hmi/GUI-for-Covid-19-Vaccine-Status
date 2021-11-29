import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',port=3306,user='root', password='', database= 'coviddata')

print(mydb)

if(mydb):
    print("Connection Suceessful")
else:
    print("Connection unsuccessful")