""" SQL wrappers """

import sqlite3
import context
import qy_factories as factories

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    return sqlite3.connect(db_file)


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
    if conn is not None:
        # create projects table
        create_table(conn, factories.create_db_qy(table, fields))
    else:
        print("Error! cannot create the database connection.")


def insert_into(db, tb, data):
    """ Wrapper function for inserting data into a SQL db/tb """
    conn = create_connection(db)
    conn.executemany(factories.insert_into_qy(tb, data['cols']), data['data'])
    conn.commit()
    conn.close()


def get_all_from_sql(database, table):
    """ Wrapper function for selecting and returning all from a SQL db/tb """
    conn = create_connection(database)
    v = conn.execute(factories.get_all_from_sql_qy(table)).fetchall()
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