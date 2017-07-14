""" SQL wrappers """

import sqlite3
import context
import os
import app.lib.sqlite.qy_factories as factories
from app.lib.tools.generalreturn import *


def throw_sqlite_error(message):
    message = 'SQLITE: ' + message
    raise ValueError(message)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    return sqlite3.connect(db_file)


def delete_database(db_file):
    """ Delete a database file """
    os.remove(db_file)
    return not does_database_exist(db_file)


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)


def create_db(database, table, fields):
    """ Wrapper function for creating a SQL table """
    # create a database connection
    conn = create_connection(database)

    # create projects table
    create_table(conn, factories.create_db_qy(table, fields))


def insert_into(db, tb, data):
    """ Interface: Inserting data into a SQL db/tb """
    conn = create_connection(db)
    conn.executemany(factories.insert_into_qy(tb, data['cols']), data['data'])
    conn.commit()
    conn.close()


def does_table_exist(database, table):
    """ Does the SQL table exist.
    Also validates the existence of the database.

    HAS_SERVICE_TESTS

    Args:
    ----
        database (str): The database where the table is expected to exist.
        
        table (str): The table whose existence is to be validated.
    Returns:
    -------
        generalreturn('No database'): If the database does not exist.

        bool: True or False, depending on whether or not the table exists.
    """
    
    # Validate existence of the database
    if not does_database_exist(database):
        return generalreturn(message='No database')
    conn = create_connection(database)
    data = conn.execute(factories.select_table_name_from_db_qy(database,table)).fetchall()
    conn.close()
    nresults = len(data)
    if nresults > 0:
        return data[0][0] == table
    else:
        return False

def does_database_exist(database):
    """ Check whether or not a SQL-lite database file exists 
    """
    # HAS_SERVICE_TESTS
    return os.path.isfile(database)

def get_all_from_sql(database, table, order=None):
    """
    Wrapper function for selecting and returning all from a SQL db/tb.

    database: The database from which to select
    table:    The table from which to select
    """
    conn = create_connection(database)
    v = conn.execute(factories.get_all_from_sql_qy(table, order)).fetchall()
    conn.close()
    return v

"""
table_fields = [
    {'name' : 'id', 'type' : 'integer primary key'},
    {'name': 'person', 'type': 'text'},
    {'name': 'age', 'type': 'integer'}
]


database = "example.db"
table = "people"


insert_data = {
    'cols': ['person', 'age'],
    'data': [
        ('jonny', 29), ('iona', 26)
    ]
}


def main():
    create_db(database, table, table_fields)
    insert_into(database, table, insert_data)
    print get_all_from_sql(database, table)


if __name__ == '__main__':
    main()
"""