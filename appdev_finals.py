import sqlite3
import time

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

# Add User
quit_program = False

while True:
    print('=== WELCOME TO THE STUDENT DATABASE ===')

    print('\n>> Main Menu <<\n')
    print('[1] ADD STUDENT')
    print('[2] SEARCH STUDENT')
    print('[3] EDIT STUDENT')
    print('[4] DELETE STUDENT')
    print('[5] DISPLAY ALL STUDENTS')
    print('[6] DISPLAY SECTIONS')
    print('[7] EXIT')

    choice = input('\nEnter a choice [1-7]: ')

    if choice == '1':
        print('>> ADD STUDENT << ')
        first_name = input('Enter the Student\'s first name: ')
        last_name = input('Enter the Student\'s last name: ')
        email = input('Enter the Student\'s email address: ')
        section = input('Enter the Student\'s section: ')

        statement = ('''
            INSERT INTO students (first_name, last_name, email, section)
            VALUES (?, ?, ?, ?)
        ''')
        data_tuple = (first_name, last_name, email, section)

        cursor.execute(statement, data_tuple)
        connection.commit()

    elif choice == '7':
        break
    else:
        print('\n ** INVALID CHOICE! Please enter a number from 1-7. **\n')

    time.sleep(5)

print('\n=== THANKS FOR USING THE STUDENT DATABASE ===')
time.sleep(5)
connection.close()
