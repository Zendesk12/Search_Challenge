
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
            # For each column in query 1
            for name in q_1.keys():
                print(f'{name:<20} {q_1[str(name)]:<20}')
            # For each column in query 2
            for q_2 in range(len(query_2)):
                if tuple(query_2[q_2])[0] == q_1['_id']:
                    print(f'ticket_{str(q_2):<13} {tuple(query_2[q_2])[1]:<20}')
            # For each column in query 3
            for q_3 in range(len(query_3)):
                if tuple(query_3[q_3])[0] == q_1['_id']:
                    print(f'user_name_{str(q_3):<10} {tuple(query_3[q_3])[1]:<20}')
    else:
        print('No results found')

