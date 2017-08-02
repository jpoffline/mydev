""" SQL query factories """


def get_all_from_sql_qy(table, order=None, topn=None, what=None):
    """ SQL-factory: Select all data from a table """
    # HAS_UNIT_TESTS

    if what is None:
        what = '*'
    else:
        what = ', '.join(what)

    select = 'SELECT ' + what + ' ' + cat_from_tb(table)

    if order is not None:
        select += ' ORDER BY ' + order

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


def count_nrows(table, where=None):
    """ SQL-factory: count the number of rows in a table """
    count_qy = "SELECT Count(*) " + cat_from_tb(table)
    if where is not None:
        count_qy += ' WHERE ' + where 
    return count_qy + ";"

def sum_col(table, col, where=None):
    """ SQL-factory: sum a particular column in a table """
    sum_qy = "SELECT SUM(" + col + ") " + cat_from_tb(table) 
    if where is not None:
        sum_qy += ' WHERE ' + where 
    return sum_qy + ";"


def strftime(time_res, time_col):
    """
    SQL-factory: convert a particular column
    into a time-object, with a particular format.
    """
    return "strftime('" + time_res + "', " + time_col + ")"



def select_groupby_time(table, meta, where=None):
    """
    SQL-factory: Select from a table, grouping
    by a time-like column.
    """
    time_res = meta['fmt']
    timecol = meta['timecol']
    others = ', '.join(meta.get('others',''))
    qy = "SELECT " + strftime(time_res, timecol)
    if others is not '':
        qy += ', ' + others
    qy += " FROM "
    qy += table + " GROUP BY " + strftime(time_res, timecol)
    if where is not None:
        qy += ' WHERE ' + where
    
    return qy + ";"

def select_distinct_dates(table, meta):
    """ SQL factory: select the distinct dates from a table.
    """
    others = ', '.join(meta.get('others',''))
    qy = "SELECT DISTINCT " + strftime(meta['fmt'], meta['timecol'])
    if others is not '':
        qy += ', ' + others
    qy += ' FROM ' + table
    qy += ' ORDER BY ' + strftime(meta['fmt'], meta['timecol']) + ' ASC'
    return qy + ';'

def select_distinct_months(table, timecol):
    return select_distinct_dates(table, {'timecol': timecol, 'fmt': agglevel_to_format('month')})

def allowed_agg_levels():
    """ Return a list of the allowed
    aggregation levels for datetimes """
    return ['year','month','day','hour','minute']

def select_in_datetime(table, meta, datewanted,subagg=None):
    """ Select columns when a time col matches a particular time frame """
    what = ', '.join(meta['what'])
    qy = "SELECT " + what + " FROM " + table 
    qy += " WHERE " + strftime(meta['fmt'], meta['timecol']) + " = '" + datewanted + "'"
    if subagg is not None:
        qy += " GROUP BY " + strftime(agglevel_to_format(subagg), meta['timecol'])
    return qy + ";"

def agglevel_to_format(agglevel):
    """ Aggregate level to format string """
    if agglevel == 'hour':
        return '%Y-%m-%d %H'
    elif agglevel == 'minute':
        return '%Y-%m-%d %H:%M'
    elif agglevel == 'year':
        return '%Y'
    elif agglevel == 'month':
        return '%Y-%m'
    elif agglevel == 'day':
        return '%Y-%m-%d'
    else:
        return False