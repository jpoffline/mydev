""" SQL query factories """


def get_all_from_sql_qy(table):
    """ SQL-factory: Select all data from a table """
    return 'SELECT * FROM ' + table


def insert_into_qy(table, names):
    """ SQL-factory: Inserting data to a table """
    string = "INSERT INTO " + table + " (" + ','.join(names) + ") VALUES ("
    zipped = ','.join("?" * len(names))
    string = string + zipped + ");"
    return string


def create_db_qy(table_name, fields):
    """ SQL-factory: Create a table if not exists """

    zipped_fields = []
    for field in fields:
        zipped_fields.append(field['name'] + ' ' + field['type'])
    string = ' CREATE TABLE IF NOT EXISTS ' + \
        table_name + ' (' + ', '.join(zipped_fields) + ');'
    return string
