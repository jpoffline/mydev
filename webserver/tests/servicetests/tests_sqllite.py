# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


MOCK_sql_database='app/data/db/adder.db'
MOCK_sql_database_not_exist='BAD_DATABASE'
MOCK_sql_table = 'history'
MOCK_sql_table_not_exist='BAD_TABLE'


import app.lib.sqlite.sqlite_api as sql
from app.lib.tools.generalreturn import *

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
