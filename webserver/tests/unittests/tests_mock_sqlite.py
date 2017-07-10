# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test
import tests.mocks.mock_sqlite as mock_sqlite

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
        ('jonny', 29), ('iona', 26), ('person', 45)
    ]
}


def test_createTB_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)
    nrows = sql.nrows(table)
    ncols = sql.ncols(table)
    ntables = sql.ntables()
    actual = (nrows, ncols, ntables)
    expected = (0, 3, 1)
    return test.exe_test(actual, expected)

def test_createTBAndAdd_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)
    sql.insert_into(table, MOCK_insert_data)
    nrows = sql.nrows(table)
    ncols = sql.ncols(table)
    ntables = sql.ntables()
    has_pk = sql.check_pk(table)
    actual = (nrows, ncols, ntables, sql.get_colnames(table), has_pk)
    expected = (3, 3, 1, ['id', 'person', 'age'], True)
    return test.exe_test(actual, expected)

def test_getAll_mockSQLite():
    table_fields = MOCK_tb_fields
    sql = mock_sqlite.mockSQLite()
    path = MOCK_db_name
    table = MOCK_tb_name
    sql.create_db(path, table, table_fields)
    sql.insert_into(table, MOCK_insert_data)
    actual = sql.get_all_from_sql(path, table)
    expected = [
        {'data': [(0, 'jonny', 29)],  'cols': ['id', 'person', 'age']}, 
        {'data': [(1, 'iona', 26)],   'cols': ['id', 'person', 'age']}, 
        {'data': [(2, 'person', 45)], 'cols': ['id', 'person', 'age']}
    ]
    return test.exe_test(actual, expected)