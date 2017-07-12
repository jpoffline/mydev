# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


MOCK_sql_database = 'app/data/db/adder.db'
MOCK_sql_database_not_exist = 'BAD_DATABASE'
MOCK_sql_table = 'history'
MOCK_sql_table_not_exist = 'BAD_TABLE'
MOCK_CREATE_db = 'tests/scratch/mysuper.db'
MOCK_CREATE_tb = 'mytable'
MOCK_CREATE_fields = [
    {'name': 'id', 'type': 'integer primary key'},
    {'name': 'person', 'type': 'text'},
    {'name': 'age', 'type': 'integer'}
]

import app.lib.sqlite.sqlite_api as sql
from app.lib.tools.generalreturn import *


def CLEANUP_service_sqlite(db):
    if sql.delete_database(db):
        return True
    return False


def service_FailOnDB_does_table_exist():
    actual = sql.does_table_exist(MOCK_sql_database_not_exist, MOCK_sql_table)
    expected = generalreturn('No database')
    return test.exe_test(actual, expected)


def service_does_table_exist():
    actual = sql.does_table_exist(MOCK_sql_database, MOCK_sql_table)
    expected = True
    return test.exe_test(actual, expected)


def service_False_does_table_exist():
    actual = sql.does_table_exist(MOCK_sql_database, MOCK_sql_table_not_exist)
    expected = False
    return test.exe_test(actual, expected)


def service_True_does_database_exist():
    actual = sql.does_database_exist(MOCK_sql_database)
    expected = True
    return test.exe_test(actual, expected)


def service_False_does_database_exist():
    actual = sql.does_database_exist(MOCK_sql_database_not_exist)
    expected = False
    return test.exe_test(actual, expected)


def service_createDB():

    sql.create_db(MOCK_CREATE_db, MOCK_CREATE_tb, MOCK_CREATE_fields)

    insert_data = {
        'cols': ['person', 'age'],
        'data': [
            ('jonny', 29), ('iona', 26)
        ]
    }
    sql.insert_into(MOCK_CREATE_db, MOCK_CREATE_tb, insert_data)
    expected = True
    actual = sql.does_table_exist(MOCK_CREATE_db, MOCK_CREATE_tb)
    CLEANUP_service_sqlite(MOCK_CREATE_db)

    return test.exe_test(actual, expected)


def service_check_sqlite_returns():

    sql.create_db(MOCK_CREATE_db, MOCK_CREATE_tb, MOCK_CREATE_fields)

    insert_data = {
        'cols': ['person', 'age'],
        'data': [
            ('jonny', 29), ('iona', 26), ('thingy', 12)
        ]
    }

    sql.insert_into(MOCK_CREATE_db, MOCK_CREATE_tb, insert_data)
    actual = sql.get_all_from_sql(MOCK_CREATE_db, MOCK_CREATE_tb)
    expected = [(1, u'jonny', 29), (2, u'iona', 26), (3, u'thingy', 12)]
    CLEANUP_service_sqlite(MOCK_CREATE_db)

    return test.exe_test(actual, expected)
