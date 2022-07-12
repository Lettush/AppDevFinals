import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS 
        students
        (
            student_no INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT, 
            last_name TEXT, 
            email TEXT,  
            section TEXT
        )
''')

connection.commit()
connection.close()