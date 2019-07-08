import sqlite3
from sqlite3 import Error
import json
from datetime import datetime


# Create a database connection to a SQLite database 

def create_connection():
    '''
    :param db_file: Data base file path 
    '''
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


# Create a database from Json data files

def create_data_base(json_files):
    '''
    :param json_file: List with the names of the json files
    '''

    conn = create_connection()

    print("insert has started at " + str(datetime.now()))

    # for each json file
    for json_f in json_files:
        with open('../Search_challenge/Json_Data/' + json_f, encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())

        # Extract columns names
        columns = extract_columns_name(json_data)

        # Extract data values
        values = extract_data_values(json_data, columns)

        # Extract table name
        table_name = json_f.split('.')[0]

        # Implement sql queries
        create_query = "create table if not exists " + table_name + " ({0})".format(" text,".join(columns))
        insert_query = "insert into " + table_name + " ({0})values(?{1})".format(", ".join(columns),
                                                                                 ",?" * (len(columns) - 1))

        # Execute sql queries
        c = conn.cursor()
        try:
            c.execute(create_query)
            c.executemany(insert_query, values)
        except sqlite3.OperationalError as e:
            print(e)

        values.clear()
        conn.commit()
        c.close()
        print("insert table " + table_name + " has completed")
    print("insert has completed at " + str(datetime.now()))

    conn.row_factory = sqlite3.Row

    return conn


# Extract columns names

def extract_columns_name(json_data):
    # Extract columns names
    columns = []
    column = []
    for data in json_data:
        column = list(data.keys())
        for col in column:
            if col not in columns:
                columns.append(col)


    return columns


# Extract data values

def extract_data_values(json_data, columns):
    # Extract data values
    value = []
    values = []
    for data in json_data:
        for i in columns:
            value.append(str(dict(data).get(i)))
        values.append(list(value))
        value.clear()


    return values