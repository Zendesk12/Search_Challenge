import sqlite3

from sqlite3 import Error
import database

'''This file contains the  search funtions of the application.'''

# Query in users table

def search_by_user(conn, search_attr, search_value=None):
    """
    :param conn: connection object with the data base
    :param search_attr: name of the column to search
    :param search_value: value to search
    """

    conn.row_factory = sqlite3.Row

    # Search users values and organization values
    try:
        cursor_1 = conn.execute(
            "SELECT users.*, organizations.name AS organization_name "
            "FROM users "
            "INNER JOIN organizations "
            "ON (users.organization_id=organizations._id)  "
            "WHERE users.{}=\"{}\"".format(search_attr, search_value))
    except sqlite3.OperationalError as e:
        print(e)

    users_and_organizations = cursor_1.fetchall()

    try:
        cursor_2 = conn.execute(
            "SELECT submitter_id, subject "
            "FROM tickets "
            "WHERE submitter_id IN "
            "(SELECT users._id "
            "FROM users"
            " WHERE {}=\"{}\")".format(search_attr, search_value))
    except sqlite3.OperationalError as e:
        print(e)

    tickets = cursor_2.fetchall()

    return users_and_organizations, tickets

# Query in organizations table

def search_by_organization(conn, search_attr, search_value=None):
    """
        :param conn: connection object with the data base
        :param search_attr: name of the column to search
        :param search_value: value to search
    """
    conn.row_factory = sqlite3.Row

    # Search organization values
    try:
        cursor_1 = conn.execute(
            "SELECT * "
            "FROM organizations "
            "WHERE {}=\"{}\"".format(search_attr, search_value))
    except sqlite3.OperationalError as e:
        print(e)

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
    except sqlite3.OperationalError as e:
        print(e)

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
    except sqlite3.OperationalError as e:
        print(e)

    users = cursor_3.fetchall()

    return organizations, tickets, users

# Query in tickets table

def search_by_tickets(conn, search_attr, search_value=None):
    """
        :param conn: connection object with the data base
        :param search_attr: name of the column to search
        :param search_value: value to search
    """
    conn.row_factory = sqlite3.Row

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
    except sqlite3.OperationalError as e:
        print(e)

    tickets = cursor_1.fetchall()

    return tickets






