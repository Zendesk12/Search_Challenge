
'''This file contains the print funtion of the application.'''


def print_query(query_1, query_2=[], query_3=[]):
    """
    :param query_1: main query
    :param query_2: tickets query (Optional)
    :param query_3: users query (Optional)
    """
    # Check if the main query is empty
    if len(query_1) != 0:
        # For each item in the query
        for q_1 in query_1:
            q2_item = 0
            q3_item = 0
            # For each column in query 1
            for name in q_1.keys():
                print(f'{name:<20} {q_1[str(name)]:<20}')
            # For each column in query 2
            for q_2 in query_2:
                if tuple(q_2)[0] == q_1['_id']:
                    print(f'ticket_{str(q2_item):<13} {tuple(q_2)[1]:<20}')
                    q2_item += 1
            # For each column in query 3
            for q_3 in query_3:
                if tuple(q_3)[0] == q_1['_id']:
                    print(f'user_name_{str(q3_item):<10} {tuple(q_3)[1]:<20}')
                    q3_item += 1
    else:
        print('No results found')

# Print Searchable Fields

def print_searchable_fields(users_fields, organizations_fields, tickets_fields):
    """
    :param users_fields: users columns
    :param organizations_fields: organizations columns
    :param tickets_fields: tickets columns
    """

    # Print users fields
    print('------------------------------')
    print('Search Users with')
    for u in users_fields:
        print(u)

    # Print oranizations fields
    print('-----------------------------')
    print('Search Organizations with')
    for o in organizations_fields:
        print(o)

    # Print tickets fields
    print('-----------------------------')
    print('Search tickets with')
    for t in tickets_fields:
        print(t)

