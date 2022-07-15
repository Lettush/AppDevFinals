import re
import sqlite3
from tabulate import tabulate

from display import display_empty_db, display_invalid_choice, display_success

# Global Variables
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

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

# Checkers
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


# >> CRUD OPERATIONS <<
# Add Student
def add_student():

    print('\n>> ADD STUDENT << ')

    # Gets student information
    first_name = input('Enter the Student\'s first name: ').title()
    last_name = input('Enter the Student\'s last name: ').title()

    # Email Validation
    while True:
        email = input('Enter the Student\'s email address: ')
        if check_email(email):
            break

    section = input('Enter the Student\'s section: ').upper()

    # Database validation
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

    # Executes SQL Query
    cursor.execute(statement, data_tuple)

    # Saves changes to DB
    connection.commit()

    # Success Message
    display_success("add", "")

# Search Student
def search_student():

    # Database validation
    if check_empty_database():
        return display_empty_db

    print('\n>> SEARCH STUDENTS <<')

    while True:
        search_choice = int(input('Would you like to search using [1] Student Number or [2] Last Name?: '))

        # For student_no search
        if search_choice == 1:
            student_no = int(input('Enter the student number of the student: '))

            # SQL Query
            cursor.execute('''
                SELECT * FROM students WHERE student_no = ?
            ''', (student_no,))

            # Fetches results from SQL Query
            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {student_no}. Try a different student number. **')

            # Tabulates results
            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))
            break
        
        # For last_name search
        if search_choice == 2:
            last_name = input('Enter the last name of the student/s: ').title()

            # SQL Query
            cursor.execute('''
                            SELECT * FROM students WHERE last_name = ?
                        ''', (last_name,))
            
            # Fetches results from SQL Query
            result = cursor.fetchall()
            if not result:
                return print(f' ** No students were found for {last_name}. Try a different last name. **')

            # Tabulates results
            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))
            break

        # Error Message
        display_invalid_choice()

# Edit Student
def edit_student():
    # Database Validation
    if check_empty_database():
        return display_empty_db

    print('\n>> SEARCH STUDENTS <<')

    while True:
        edit_choice = int(input('Would you like to search using: [1] Student Number or [2] Last Name?: '))

        # For student_no search
        if edit_choice == 1:

            student_no = int(input('Enter the student number of the student: '))

            # SQL Query
            cursor.execute('''
                SELECT * FROM students WHERE student_no = ?
            ''', (student_no,))

            # Retrieves results from the database
            result = cursor.fetchall()
            if not result:
                return print(f' ** No students were found for {student_no}. Try a different student number. **')
            
            # Tabulates result
            print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))
            
            # Gets updated student details
            first_name = input('Enter student first name: ')
            last_name = input('Enter student last name: ')
            email_address = input('Enter email address: ')

            # Email Validation
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
            
            # Executes SQL Command
            cursor.execute(statement, data_tuple)

            # Saves the DB changes
            connection.commit()

            display_success("edit", student_no)
            break

        # For Last name search
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
            
            # Gets updated student details
            first_name = input('Enter student first name: ')
            last_name = input('Enter student last name: ')
            email_address = input('Enter email address: ')

            # Email validation
            while not check_email(email_address):
                email_address = input('Enter email address: ')               
            section = input('Enter section: ')

            # Database Validation
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

            # Executes SQL Query
            cursor.execute(statement, data_tuple)

            # Saves changes to DB
            connection.commit()

            # Success message
            display_success("edit", student_no)

            break

        # Error message
        display_invalid_choice()

# Deletes Student
def delete_student():

    # Database Validation
    if check_empty_database():
        return display_empty_db

    print('\n>> DELETE STUDENTS <<')

    while True:
            student_no = int(input('Enter the student number of the student: '))

            # SQL Query
            cursor.execute('''
                SELECT * FROM students WHERE student_no = ?
            ''', (student_no,))

            # Retrieves results from SQL query
            result = cursor.fetchall()

            if not result:
                return print(f' ** No students were found for {student_no}. Try a different student number. **')
            
            # SQL Query
            cursor.execute('''
                DELETE FROM students WHERE student_no = ?
            ''', (student_no,))

            # Saves changes to db
            connection.commit()

            # Confirmation message
            display_success("delete", student_no)
            break

# Display All Students
def display_all_students():

    # Database Validation
    if check_empty_database():
        return display_empty_db
    print('\n>> DISPLAY ALL STUDENTS << ')

    # SQL Query
    cursor.execute('''
        SELECT * FROM students
    ''')
    
    # Results from SQL
    result = cursor.fetchall()

    # Tabulates results
    print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))

# Display By Section
def display_section():

    # Database validation
    if check_empty_database():
        return display_empty_db

    print('\n>> DISPLAY SECTIONS <<')

    section = input('Enter which section should be searched: ').upper()

    # SQL Query
    cursor.execute('''
        SELECT * FROM students WHERE section = ?
    ''', (section,))

    # Results
    result = cursor.fetchall()

    if not result:
        return print(f' ** [System]: No students were found for {section}. Try a different section. **')

    # Tabulates results
    print(tabulate(result, headers=['Student No.', 'First Name', 'Last Name', 'Email Address', 'Section']))

