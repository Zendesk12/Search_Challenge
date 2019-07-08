# search_engine.py

'''This file contains the search funtions of the application.'''

# Import statements
import sqlite3
from printer import print_query, print_searchable_fields


# Query in users table

def search_by_user(conn, search_attr, search_value=None):
    """
    :param conn: connection object with the data base
    :param search_attr: name of the column to search
    :param search_value: value to search
    """
    # Initialize variables
    users_and_organizations = []
    tickets = []

    # Covert search_value to search empty fields
    if search_value == '':
        search_value = None

    # Search users values and organization values
    try:
        cursor_1 = conn.execute(
            "SELECT users.*, organizations.name AS organization_name "
            "FROM users "
            "INNER JOIN organizations "
            "ON (users.organization_id=organizations._id)  "
            "WHERE users.{}=\"{}\"".format(search_attr, search_value))
    except sqlite3.Error as e:
        print(e)
    else:
        users_and_organizations = cursor_1.fetchall()

        try:
            cursor_2 = conn.execute(
                "SELECT submitter_id, subject "
                "FROM tickets "
                "WHERE submitter_id IN "
                "(SELECT users._id "
                "FROM users"
                " WHERE {}=\"{}\")".format(search_attr, search_value))
        except sqlite3.Error as e:
            print(e)
        else:
            tickets = cursor_2.fetchall()

    # Print the result
    print_query(users_and_organizations, tickets)

    return users_and_organizations, tickets


# Query in organizations table

def search_by_organization(conn, search_attr, search_value=None):
    """
        :param conn: connection object with the data base
        :param search_attr: name of the column to search
        :param search_value: value to search
    """

    # Initialize variables
    organizations = []
    tickets = []
    users = []

    # Covert search_value to search empty fields
    if search_value == '':
        search_value = None

    # Search organization values
    try:
        cursor_1 = conn.execute(
            "SELECT * "
            "FROM organizations "
            "WHERE {}=\"{}\"".format(search_attr, search_value))
    except sqlite3.Error as e:
        print(e)
    else:
        organizations = cursor_1.fetchall()

        # Search tickets values
        try:
            cursor_2 = conn.execute(
                "SELECT organization_id, subject "
                "FROM tickets "
                "WHERE organization_id IN"
                "(SELECT organizations._id "
                "FROM organizations"
                " WHERE {}=\"{}\")".format(search_attr, search_value))
        except sqlite3.Error as e:
            print(e)
        else:
            tickets = cursor_2.fetchall()

        # Search users values
        try:
            cursor_3 = conn.execute(
                "SELECT organization_id, users.name "
                "FROM users "
                "WHERE organization_id IN "
                "(SELECT organizations._id "
                "FROM organizations "
                "WHERE {}=\"{}\")".format(search_attr, search_value))
        except sqlite3.Error as e:
            print(e)
        else:
            users = cursor_3.fetchall()

    # Print the result
    print_query(organizations, tickets, users)

    return organizations, tickets, users


# Query in tickets table

def search_by_tickets(conn, search_attr, search_value=None):
    """
        :param conn: connection object with the data base
        :param search_attr: name of the column to search
        :param search_value: value to search
    """

    # Initialize variables
    tickets = []

    # Covert search_value to search empty fields
    if search_value == '':
        search_value = None

    # Search tickets values
    try:
        cursor_1 = conn.execute(
            "SELECT tickets.*, "
            "organizations.name AS organization_name , "
            "users.name AS user_name "
            "FROM tickets "
            "INNER JOIN users "
            "ON (tickets.submitter_id=users._id)  "
            "INNER JOIN organizations "
            "ON (tickets.organization_id=organizations._id)"
            " WHERE tickets.{}=\"{}\"".format(search_attr, search_value))
    except sqlite3.Error as e:
        print(e)
    else:
        tickets = cursor_1.fetchall()

    # Print the result
    print_query(tickets)

    return tickets


# Query in the data base to extract searchable fiels

def searchable_fields(conn):
    """
        :param conn: connection object with the data base
    """

    try:
        cursor_1 = conn.execute(
            "SELECT * FROM users ")
    except sqlite3.Error as e:
        print(e)

    users_fields = cursor_1.fetchone().keys()

    try:
        cursor_2 = conn.execute(
            "SELECT * FROM organizations ")
    except sqlite3.Error as e:
        print(e)

    organizations_fields = cursor_2.fetchone().keys()

    try:
        cursor_3 = conn.execute(
            "SELECT * FROM tickets ")
    except sqlite3.Error as e:
        print(e)

    tickets_fields = cursor_3.fetchone().keys()

    print_searchable_fields(users_fields, organizations_fields, tickets_fields)

    return 1

