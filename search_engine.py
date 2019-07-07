import sqlite3

from sqlite3 import Error

'''This file contains the  search funtions of the application.'''

# Query in users data base

def search_by_user(conn, search_attr, search_value):
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
        print(e.message)

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
        print(e.message)

    tickets = cursor_2.fetchall()

    return users_and_organizations, tickets
