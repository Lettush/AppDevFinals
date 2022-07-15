import time
from db_operations import *
from display import display_menu

print('\n=== WELCOME TO THE STUDENT DATABASE ===')
while True:

    # Displays choice menu
    display_menu()

    choice = int(input('\nEnter a choice [1-7]: '))

    # Checks for user choice
    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_all_students()
    elif choice == 6:
        display_section()
    elif choice == 7:
        break
    else:
        print('\n ** [System]: INVALID CHOICE! Please enter a number from 1-7. **\n')

    time.sleep(2.5)

# Exit Message
print('\n>>> THANKS FOR USING THE STUDENT DATABASE <<<')
time.sleep(2.5)

# Closes DB Connection
connection.close()
