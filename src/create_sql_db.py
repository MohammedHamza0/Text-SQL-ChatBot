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
cursor.execute(table_info)


## insert data into the table
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('John', 20, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jane', 21, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jim', 22, 'C')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jill', 23, 'D')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jack', 24, 'E')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Judy', 25, 'F')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Joe', 26, 'G')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jasmine', 27, 'H')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jordan', 28, 'I')")



## show the inserted data
data = cursor.execute("SELECT * FROM students")

for row in data:
     print(row)
     
     
     


## commit the changes to the database
conneciton.commit()

## close the connection to the database
conneciton.close()


print("Database created successfully!")


