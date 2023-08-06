# CREATE database python_db;

# CREATE TABLE Hospital (
#     Hospital_Id INT UNSIGNED NOT NULL, 
#     Hospital_Name TEXT NOT NULL, 
#     Bed_Count INT, 
#     PRIMARY KEY (Hospital_Id)
# );

# INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
# VALUES 
# ('1', 'Mayo Clinic', 200), 
# ('2', 'Cleveland Clinic', 400), 
# ('3', 'Johns Hopkins', 1000), 
# ('4', 'UCLA Medical Center', 1500);

# CREATE TABLE Doctor(
#     Doctor_Id INT UNSIGNED NOT NULL,
#     Doctor_Name TEXT NOT NULL, 
#     Hospital_Id INT NOT NULL, 
#     Joining_Date DATE NOT NULL, 
#     Speciality TEXT NULL, 
#     Salary INT NULL, 
#     Experience INT NULL, 
#     PRIMARY KEY (Doctor_Id)
# );

# INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
# VALUES 
# ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
# ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
# ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
# ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
# ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
# ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
# ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
# ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);

#Question 1 - Fetch Hospital and Doctor Information using hospital Id and doctor Id
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='C@non1300d')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 1: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)

#Question 2 - Get the list Of doctors as per the given specialty and salary

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Doctor where Speciality=%s and Salary > %s"""
        cursor.execute(sql_select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 2: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Garnacologist", 30000)

#Question 3 - Get a list of doctors from a given hospital
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_name(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (hospital_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctors(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        hospital_name = get_hospital_name(hospital_id)
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Doctor where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (hospital_id,))
        records = cursor.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 3:  Get List of doctors of a given Hospital Id\n")
get_doctors(2)

#Question 4 - Update doctor experience in years
import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def update_doctor_experience(doctor_id):
    # Update Doctor Experience in Years
    try:
        # Get joining date
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select Joining_Date from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        joining_date = cursor.fetchone()

        # calculate Experience in years
        joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date = datetime.datetime.now()
        experience = relativedelta(today_date, joining_date_1).years

        # Update doctor's Experience now
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
        cursor.execute(sql_select_query, (experience, doctor_id))
        connection.commit()
        print("Doctor Id:", doctor_id, " Experience updated to ", experience, " years")
        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 4: Calculate and Update experience of all doctors  \n")
update_doctor_experience(101)