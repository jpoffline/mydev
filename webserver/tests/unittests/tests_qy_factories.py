# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


import app.lib.sqlite.qy_factories as qy_factories


def test_order_get_all_from_sql_qy():
    table = 'TABLE'
    ord = 'id desc'
    actual = qy_factories.get_all_from_sql_qy(table, order=ord)
    expected = 'SELECT * FROM TABLE ORDER BY id desc'
    return test.exe_test(actual, expected)


def test_get_all_from_sql_qy():
    table = 'TABLE'
    actual = qy_factories.get_all_from_sql_qy(table)
    expected = 'SELECT * FROM TABLE'
    return test.exe_test(actual, expected)

def test_top_get_all_from_sql_qy():
    table = 'TABLE'
    actual = qy_factories.get_all_from_sql_qy(table, topn=5)
    expected = 'SELECT * FROM TABLE LIMIT 5'
    return test.exe_test(actual, expected)


def test_emptyNames_insert_into_qy():
    table = 'TABLE'
    names = []
    actual = qy_factories.insert_into_qy(table, names)
    expected = 'INSERT INTO TABLE () VALUES ();'
    return test.exe_test(actual, expected)


def test_withNames_insert_into_qy():
    table = 'TABLE'
    names = ['col1', 'col2']
    actual = qy_factories.insert_into_qy(table, names)
    expected = 'INSERT INTO TABLE (col1,col2) VALUES (?,?);'
    return test.exe_test(actual, expected)


def test_emptyFields_create_db_qy():
    table = 'TABLE_NAME'
    fields = []
    actual = qy_factories.create_db_qy(table, fields)
    expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME ();'
    return test.exe_test(actual, expected)


def test_withOneField_create_db_qy():
    table = 'TABLE_NAME'
    fields = [{'name': 'col1', 'type': 'TYPE1'}]
    actual = qy_factories.create_db_qy(table, fields)
    expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME (col1 TYPE1);'
    return test.exe_test(actual, expected)


def test_withManyFields_create_db_qy():
    table = 'TABLE_NAME'
    fields = [
        {
            'name': 'col1',
            'type': 'TYPE1'
        },
        {
            'name': 'col2',
            'type': 'TYPE2'
        }
    ]
    actual = qy_factories.create_db_qy(table, fields)
    expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME (col1 TYPE1, col2 TYPE2);'
    return test.exe_test(actual, expected)