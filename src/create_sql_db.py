import sqlite3


## connect to the database
conneciton = sqlite3.connect("database/students.db")


## create a cursor object to create tables and execute SQL commands
cursor = conneciton.cursor()




## create a table
table_info = """    CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
               )
               """
               
doctor_tabel_info = """    CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    specialization TEXT NOT NULL
               )
               """               

cursor.execute(table_info)
cursor.execute(doctor_tabel_info)


## insert data into the table
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('John', 20, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jane', 21, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jim', 22, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jill', 23, 'D')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jack', 24, 'E')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Judy', 25, 'F')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Joe', 26, 'G')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jasmine', 27, 'H')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jordan', 28, 'I')")


# insert into doctors table
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Smith', 40, 'Cardiology')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Brown', 45, 'Neurology')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Taylor', 50, 'Orthopedics')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Wilson', 55, 'Pediatrics')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Johnson', 60, 'Dermatology')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Lee', 65, 'Radiology')")
cursor.execute("INSERT INTO doctors (name, age, specialization) VALUES ('Dr. Davis', 70, 'Oncology')")



## show the inserted data
data = cursor.execute("SELECT * FROM students")

for row in data:
     print(row)
     
data = cursor.execute("SELECT * FROM doctors")
for row in data:
     print(row)
     
     
     


## commit the changes to the database
conneciton.commit()

## close the connection to the database
conneciton.close()


print("Database created successfully!")


