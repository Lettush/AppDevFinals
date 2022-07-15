def display_menu():
    print('\n>> Main Menu <<\n')
    print('[1] ADD STUDENT')
    print('[2] SEARCH STUDENT')
    print('[3] EDIT STUDENT')
    print('[4] DELETE STUDENT')
    print('[5] DISPLAY ALL STUDENTS')
    print('[6] DISPLAY SECTIONS')
    print('[7] EXIT')

def display_success(msg_type, student_no):
    message = "\nStudent has been ";
    switcher = {
        "add": "added successfully!",
        "edit": "edited successfully! (Student # " + str(student_no) +")",
        "delete": "deleted successfully! (Student # " + str(student_no) +")",
    }
    message += switcher.get(msg_type)

    print(message);

def display_empty_db():
    print('** [System]: Database is empty! **')

def display_invalid_choice():
    print('[System]: Invalid choice.')