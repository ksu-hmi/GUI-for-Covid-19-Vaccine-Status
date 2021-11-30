#you must have MySQL installed and running on the host indicated below with the database loaded from the SQL file here first or this code will not run when you try
import pymysql as my

#root password is something you set when you install mysql on your system
#the default may be blank; I used python123 for testing
#BE SURE to match your password to the password you set when installing MySQL. If in doubt, try a blank password
dbconn = my.connect (host='127.0.0.1',port=3306,user='root', password='',  db='coviddata')
 
#print(dbconn) #This is a testing stub to make sure the connection worked. Uncomment it to use it.
cursor = dbconn.cursor()
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
cursor = dbconn.cursor()
query = "SELECT * FROM covid_info"
cursor.execute(query)
vaccine = []
for (Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN) in cursor:
    vac_dose = [Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN]
    vac_dose.append(vac_dose)
dbconn.close()

print(users)

#print(users[5][1],users[5][2])

print(vaccine)


#print(str(vaccine[0][1])+" is of type "+str(type(vaccine[0][1])))
