# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test
import tests.mocks.mock_sqlite as mock_sqlite
from app.lib.tools.generalreturn import *

MOCK_db_name = 'PATH'
MOCK_tb_name = 'TABLE'
MOCK_tb_fields = [
    {'name': 'id', 'type': 'integer primary key'},
    {'name': 'person', 'type': 'text'},
    {'name': 'age', 'type': 'integer'}
]
MOCK_insert_data = {
    'cols': ['person', 'age'],
    'data': [
        ('jonny', 29), ('iona', 26), ('thingy', 12)
    ]
}


def test_createTB_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)

    actual = {
        'nrows': sql.nrows(table),
        'ntables': sql.ntables(),
        'ncols': sql.ncols(table)
        
    }

    expected = {
        'nrows': 0,
        'ncols': 3,
        'ntables':1
    }
    return test.exe_test(actual, expected)

def test_createTBAndAdd_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)
    # Insert some data
    insert_ok = sql.insert_into(table, MOCK_insert_data)

    actual = {
        'nrows': sql.nrows(table),
        'ncols': sql.ncols(table),
        'ntables': sql.ntables(),
        'col_names': sql.get_colnames(table),
        'has_pk': sql.check_pk(table),
        'insert_ok': insert_ok
    }

    expected = {
        'nrows': 3,
        'ncols': 3,
        'ntables': 1,
        'col_names': ['id', 'person', 'age'],
        'has_pk': False,
        'insert_ok': True
    }

    return test.exe_test(actual, expected, many = True)

def test_getAll_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)
    sql.insert_into(table, MOCK_insert_data)
    actual = sql.get_all_from_sql(path, table)
    expected = [(1, u'jonny', 29), (2, u'iona', 26), (3, u'thingy', 12)]
    return test.exe_test(actual, expected)


def test_badData_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    insert_data = {
        'cols': ['person', 'age'],
        'data': [
            ('jonny', 29), 
            ('iona', 26, 89), 
            ('thingy', 12)
        ]
    }
    sql.create_db(path, table, table_fields)
    actual = sql.insert_into(table, insert_data)
    expected = generalreturn('MOCK_SQLITE ERROR<add_row>: unexpected number of elements')
    return test.exe_test(actual, expected)
