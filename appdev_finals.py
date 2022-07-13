import sqlite3
import time
from tabulate import tabulate
import re

# DB Connection
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
quit_program = False
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check_email(email):
    if re.fullmatch(email_regex, email):
        return True
    else:
        print('\nINVALID EMAIL! Please enter a valid email address.\n')
        return False


def check_empty_database():
    cursor.execute('''
                    SELECT COUNT(*) from students
                ''')
    result = cursor.fetchall()

    if result[0][0] == 0:
        # Database is Empty
        return True
    return False


# Add Students
def add_student():
    print('\n>> ADD STUDENT << ')
    first_name = input('Enter the Student\'s first name: ').title()
    last_name = input('Enter the Student\'s last name: ').title()

    while True:
        email = input('Enter the Student\'s email address: ')

        if check_email(email):
            break

    section = input('Enter the Student\'s section: ').upper()

    if check_empty_database():
        statement = ('''
                                INSERT INTO students (student_no, first_name, last_name, email, section)
                                VALUES (202200001, ?, ?, ?, ?)
                            ''')
        data_tuple = (first_name, last_name, email, section)

    else:
        statement = ('''
                    INSERT INTO students (first_name, last_name, email, section)
                    VALUES (?, ?, ?, ?)
                ''')
        data_tuple = (first_name, last_name, email, section)

    cursor.execute(statement, data_tuple)
    connection.commit()

    print('\n[System]: Student has been added successfully!')

# Search Student
def search_student():
    if check_empty_database():
        return print(' ** Database is empty! **')

    print('\n>> SEARCH STUDENTS <<')
    while True:
        search_choice = int(input('Would you like to search using [1] Student Number or [2] Last Name?: '))

        if search_choice == 1:
            student_no = int(input('Enter the student number of the student: '))
            cursor.execute('''
                SELECT * FROM students WHERE student_no = ?
            ''', (student_no,))

            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {student_no}. Try a different student number. **')

            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))
            break
        if search_choice == 2:
            last_name = input('Enter the last name of the student/s: ').title()
            cursor.execute('''
                            SELECT * FROM students WHERE last_name = ?
                        ''', (last_name,))

            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {last_name}. Try a different last name. **')

            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))
            break
        print('[System]: Invalid choice.')

# Edit Student
def edit_student():
    if check_empty_database():
        return print(' ** Database is empty! **')

    print('\n>> SEARCH STUDENTS <<')
    while True:
        edit_choice = int(input('Would you like to search using: [1] Student Number or [2] Last Name?: '))

        if edit_choice == 1:
            student_no = int(input('Enter the student number of the student: '))
            cursor.execute('''
                SELECT * FROM students WHERE student_no = ?
            ''', (student_no,))

            # Retrieves results from the database
            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {student_no}. Try a different student number. **')

            # Tabulates result
            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))

            # Updates student details
            first_name = input('Enter student first name: ')
            last_name = input('Enter student last name: ')
            email_address = input('Enter email address: ')

            # Checks if email is valid
            # Checks if email is valid
            while not check_email(email_address):
                email_address = input('Enter email address: ')  

            section = input('Enter section: ')

            if check_empty_database():
                statement = ('''
                            UPDATE Students SET first_name = ?, last_name = ?, email = ?, section = ?
                            WHERE student_no = ?
                ''')
                data_tuple = (first_name, last_name, email_address, section, student_no)

            else:
                statement = ('''
                            UPDATE Students SET first_name = ?, last_name = ?, email = ?, section = ?
                            WHERE student_no = ?
                ''')
                data_tuple = (first_name, last_name, email_address, section, student_no)

            cursor.execute(statement, data_tuple)
            connection.commit()

            print('\n[System]: Student has edited successfully!')

            break
        if edit_choice == 2:
            last_name = input('Enter the last name of the student/s: ').title()
            cursor.execute('''
                            SELECT * FROM students WHERE last_name = ?
                        ''', (last_name,))

            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {last_name}. Try a different last name. **')

            # Tabulates result
            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))

            # Updates student details
            first_name = input('Enter student first name: ')
            last_name = input('Enter student last name: ')
            email_address = input('Enter email address: ')

            # Checks if email is valid
            while not check_email(email_address):
                email_address = input('Enter email address: ')               

            section = input('Enter section: ')

            if check_empty_database():
                statement = ('''
                            UPDATE Students SET first_name = ?, last_name = ?, email = ?, section = ?
                            WHERE last_name = ?
                ''')
                data_tuple = (first_name, last_name, email_address, section, last_name)

            else:
                statement = ('''
                            UPDATE Students SET first_name = ?, last_name = ?, email = ?, section = ?
                            WHERE last_name = ?
                ''')
                data_tuple = (first_name, last_name, email_address, section, last_name)

            cursor.execute(statement, data_tuple)
            connection.commit()

            print('\n[System]: User has edited successfully!')

            break
        print('Invalid choice.')

# Display All Students
def display_all_students():
    if check_empty_database():
        return print(' ** Database is empty! **')

    print('\n>> DISPLAY ALL STUDENTS << ')
    cursor.execute('''
        SELECT * FROM students
    ''')
    result = cursor.fetchall()

    print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))


# Display Section
def display_section():
    if check_empty_database():
        return print(' ** Database is empty! **')

    print('\n>> DISPLAY SECTIONS <<')
    section = input('Enter which section should be searched: ').upper()

    cursor.execute('''
        SELECT * FROM students WHERE section = ?
    ''', (section,))
    result = cursor.fetchall()

    if not result:
        return print(f' ** No students were found for {section}. Try a different section. **')

    print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))


print('\n=== WELCOME TO THE STUDENT DATABASE ===')
while True:
    print('\n>> Main Menu <<\n')
    print('[1] ADD STUDENT')
    print('[2] SEARCH STUDENT')
    print('[3] EDIT STUDENT')
    print('[4] DELETE STUDENT')
    print('[5] DISPLAY ALL STUDENTS')
    print('[6] DISPLAY SECTIONS')
    print('[7] EXIT')

    choice = int(input('\nEnter a choice [1-7]: '))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        edit_student()
    elif choice == 5:
        display_all_students()
    elif choice == 6:
        display_section()
    elif choice == 7:
        break
    else:
        print('\n ** INVALID CHOICE! Please enter a number from 1-7. **\n')

    time.sleep(2.5)

# Exit Message
print('\n>>> THANKS FOR USING THE STUDENT DATABASE <<<')
time.sleep(2.5)
connection.close()
