import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',port=3306,user='root', password='', database= 'coviddata')

print(mydb)

if(mydb):
    print("Connection Suceessful")
else:
    print("Connection unsuccessful")


cursor = mydb.cursor()
query = "SELECT FirstName, LastName, DOB, Vac_status from covid_info join patient_demo on patient_demo.MRN = covid_info.patient_demo_MRN"
cursor.execute(query)
#the following line shows the schema descriptions of the headers of the data retrieved in the cursor object from the database using the query
print(cursor.description)


users = []

for (FirstName, LastName, DOB, Vac_status) in cursor:
    print("{} {} ({}) found. Vaccination Status {}.".format(FirstName, LastName, DOB, Vac_status))
    thisuser = [FirstName, LastName, DOB, Vac_status]
    users.append(thisuser)
cursor.close()
cursor = mydb.cursor()
query = "SELECT * FROM covid_info"
cursor.execute(query)
vaccine = []
for (Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN) in cursor:
    vac_dose = [Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN]
    vac_dose.append(vac_dose)
mydb.close()

print(users)

#print(users[5][1],users[5][2])

print(vaccine)


#print(str(vaccine[0][1])+" is of type "+str(type(vaccine[0][1])))
