import sqlite3
import json

from sqlite3 import Error
from datetime import datetime


# Create a database connection to a SQLite database

def create_connection(db_file):
    """
    :param db_file: Data base file path
    """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


# Create a database from Json data files

def create_data_base(db_file, json_files):
    """
    :param db_file: Data base file path
    :param json_files: List with the names of the json files
    """

    conn = create_connection(db_file)

    print("insert has started at " + str(datetime.now()))

    # for each json file
    for json_f in json_files:
        try:
            with open('../Search_challenge/Json_Data/' + json_f,
                    encoding='utf-8-sig') as json_file:
                json_data = json.loads(json_file.read())
        except json.JSONDecodeError:
            print 'Decoding JSON has failed'

        # Extract columns names
        columns = []
        column = []
        for data in json_data:
            column = list(data.keys())
            for col in column:
                if col not in columns:
                    columns.append(col)

        # Extract data values
        value = []
        values = []
        for data in json_data:
            for i in columns:
                value.append(str(dict(data).get(i)))
            values.append(list(value))
            value.clear()

        # Extract table name
        table_name = json_f.split('.')[0]

        # Implement sql queries
        create_query = "create table if not exists " + table_name + \
                       " ({0})".format(" text,".join(columns))
        insert_query = "insert into " + table_name + \
                       " ({0})values(?{1})".format(", ".join(columns), ",?"
                                                   * (len(columns) - 1))

        # Execute sql queries
        c = conn.cursor()
        c.execute(create_query)
        c.executemany(insert_query, values)
        values.clear()
        conn.commit()
        c.close()
        print("insert table " + table_name + " has completed")
    print("insert has completed at " + str(datetime.now()))
