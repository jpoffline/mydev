""" SQL query factories """


def get_all_from_sql_qy(table, order=None, topn=None):
    """ SQL-factory: Select all data from a table """
    # HAS_UNIT_TESTS
    select = 'SELECT * ' + cat_from_tb(table)

    if order is not None:
        select +=  ' ORDER BY ' + order

    if topn is not None:
        select += ' LIMIT ' + str(topn)
    return select


def cat_from_tb(table):
    """ Prepend FROM onto the table. """
    return 'FROM ' + table


def insert_into_qy(table, names):
    """ SQL-factory: inserting data to a table """
    # HAS_UNIT_TESTS
    string = "INSERT INTO " + table + " (" + ','.join(names) + ") VALUES ("
    zipped = ','.join("?" * len(names))
    string = string + zipped + ");"
    return string


def create_db_qy(table_name, fields):
    """ SQL-factory: create a table if not exists """
    # HAS_UNIT_TESTS
    zipped_fields = []
    for field in fields:
        zipped_fields.append(field['name'] + ' ' + field['type'])
    string = 'CREATE TABLE IF NOT EXISTS ' + \
        table_name + ' (' + ', '.join(zipped_fields) + ');'
    return string


def select_table_name_from_db_qy(database, table):
    """ SQL-factory: select a particular table name from the database """
    return "SELECT name FROM sqlite_master " + \
        "WHERE type='table' AND name='" + table + "' LIMIT 1;"


def count_nrows(table):
    """ SQL-factory: count the number of rows in a table """
    return "SELECT Count(*) " + cat_from_tb(table) + ";"


def sum_col(table, col):
    """ SQL-factory: sum a particular column in a table """
    return "SELECT SUM(" + col + ") " + cat_from_tb(table) + ";"


def strftime(time_res, time_col):
    return "strftime('" + time_res + "', " + time_col + ")"


def select_groupby_time(table, meta):
    time_res = meta['fmt']
    timecol = meta['timecol']
    others = meta['others']
    return "SELECT " + strftime(time_res, timecol) + ", " + \
        others + " FROM " + \
        table + " GROUP BY " + strftime(time_res, timecol) +";"
