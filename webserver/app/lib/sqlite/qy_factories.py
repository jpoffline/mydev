""" SQL query factories """


def get_all_from_sql_qy(table, order=None):
    """ SQL-factory: Select all data from a table """
    # HAS_UNIT_TESTS
    if order is None:
        return 'SELECT * FROM ' + table
    else:
        return 'SELECT * FROM ' + table + ' ORDER BY ' + order


def insert_into_qy(table, names):
    """ SQL-factory: Inserting data to a table """
    # HAS_UNIT_TESTS
    string = "INSERT INTO " + table + " (" + ','.join(names) + ") VALUES ("
    zipped = ','.join("?" * len(names))
    string = string + zipped + ");"
    return string


def create_db_qy(table_name, fields):
    """ SQL-factory: Create a table if not exists """
    # HAS_UNIT_TESTS
    zipped_fields = []
    for field in fields:
        zipped_fields.append(field['name'] + ' ' + field['type'])
    string = 'CREATE TABLE IF NOT EXISTS ' + \
        table_name + ' (' + ', '.join(zipped_fields) + ');'
    return string
