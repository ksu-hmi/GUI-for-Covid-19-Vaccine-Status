#you must have MySQL installed and running on the host indicated below with the database loaded from the SQL file here first or this code will not run when you try
import pymysql as my

def db_conn():
    #root password is something you set when you install mysql on your system
    #the default may be blank; I used python123 for testing
    #BE SURE to match your password to the password you set when installing MySQL. If in doubt, try a blank password
    this_dbconn = my.connect (host='127.0.0.1',port=3306,user='root', password='',  db='coviddata')
    return this_dbconn
    
def db_query(conn=None,sql_query="SELECT FirstName, LastName, DOB, MRN, Vac_status from covid_info join patient_demo on patient_demo.MRN = covid_info.patient_demo_MRN"):
    '''
    This function takes a conn and sql_query and returns a cursor.
    '''
    
    if conn == None:
        conn = db_conn()
    #print(dbconn) #This is a testing stub to make sure the connection worked. Uncomment it to use it.
    cursor = conn.cursor()
    query = sql_query
    cursor.execute(query)
    #the following line shows the schema descriptions of the headers of the data retrieved in the cursor object from the database using the query
    print(cursor.description)
    return cursor, conn

def list_all_data(conn=None):
    if conn == None:
        conn = db_conn()
    users = []
    this_cursor, conn = db_query(conn)
    for (FirstName, LastName, DOB, MRN, Vac_status) in this_cursor:
        print("{} {} ({}) ({}) found. Vaccination Status {}.".format(FirstName, LastName, DOB, MRN, Vac_status))
        thisuser = [FirstName, LastName, DOB, MRN, Vac_status]
        users.append(thisuser)
    this_cursor.close()
    conn.close()
    return users

def find_patient_doses(conn=None,sql_query = "SELECT * FROM covid_info"):
    if conn == None:
        conn = db_conn()
    this_cursor = db_query(conn,sql_query)
    vaccine = []
    for (Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN) in this_cursor:
        vac_dose = [Vac_status, first_dose, second_dose, third_dose,patient_demo_MRN]
        vaccine.append(vac_dose)
    this_cursor.close()
    conn.close()
    return vaccine

users = list_all_data()
print(users)

#print(users[5][1],users[5][2])

vaccine = find_patient_doses()
print(vaccine)


#print(str(vaccine[0][1])+" is of type "+str(type(vaccine[0][1])))
