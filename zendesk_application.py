from database import create_data_base
from search_engine import search_by_user, search_by_organization, search_by_tickets, searchable_fields

'''This file contains the logic application function.'''

def run_application():
    # Messages
    welcome = '\n\nWelcome to Zendesk Search'
    information_text_1 = 'Type "quit" to exit at any time, Press "Enter" to continue\n'
    information_text_2 = '\t\tSelect search options:\n\t\t* Press 1 to search\n\t\t* Press 2 to view a list of ' \
                         'searchable field\n\t\t* Type "quit" to exit\n '
    information_text_3 = '\t\tSelect table:\n\t\t* Select 1 users\n\t\t* Select 2 organizations\n\t\t* Select 3 ' \
                         'tickets\n '

    # Data base initialization
    json_files = ["users.json", "organizations.json", "tickets.json"]
    connection = create_data_base(json_files)

    # Start our application
    print(f'{welcome}')

    command = input(information_text_1)
    # Exit any time
    while not command == 'quit':
    	# Client press "Enter"
        if command == '':
        	# Exit any time
            while not command == 'quit':
            	# Display options
                command = input(information_text_2)
                # Selected Search option
                if command == '1':
                	# Exit any time
                    while not command == 'quit':
                    	# Display table options
                        command = input(information_text_3)
                        # Selected users table
                        if command == '1':
                        	# Enter search column
                            search_attr = input('Enter search term\n')
                            # Enter search value
                            search_value = input('Enter search value\n')
                            # Searching
                            search_by_user(connection, search_attr, search_value)
                        # Selected organizations table
                        elif command == '2':
                        	# Enter search column
                            search_attr = input('Enter search term\n')
                            # Enter search value
                            search_value = input('Enter search value\n')
                            # Searching
                            search_by_organization(connection, search_attr, search_value)
                        # Selected tickets table
                        elif command == '3':
                        	# Enter search column
                            search_attr = input('Enter search term\n')
                            # Enter search value
                            search_value = input('Enter search value\n')
                            # Searching
                            search_by_tickets(connection, search_attr, search_value)
                # Selected Searchable  field list option
                elif command == '2':
                    searchable_fields(connection)
        else:
            command = input(information_text_1)

    # Close connection and free up the memory		
    connection.close()

    print('Good Bye')


# Run the game
if __name__ == '__main__':
    run_application()
