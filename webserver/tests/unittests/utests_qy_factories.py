# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app



import app.lib.sqlite.qy_factories as qy_factories


import unittest

class TestQyFactories(unittest.TestCase):

    def test_order_get_all_from_sql_qy(self):
        table = 'TABLE'
        ord = 'id desc'
        actual = qy_factories.get_all_from_sql_qy(table, order=ord)
        expected = 'SELECT * FROM TABLE ORDER BY id desc'
        self.assertEqual(actual, expected)    
    
    def test_get_all_from_sql_qy(self):
        table = 'TABLE'
        actual = qy_factories.get_all_from_sql_qy(table)
        expected = 'SELECT * FROM TABLE'
        self.assertEqual(actual, expected)    
    def test_top_get_all_from_sql_qy(self):
        table = 'TABLE'
        actual = qy_factories.get_all_from_sql_qy(table, topn=5)
        expected = 'SELECT * FROM TABLE LIMIT 5'
        self.assertEqual(actual, expected)    
    
    def test_emptyNames_insert_into_qy(self):
        table = 'TABLE'
        names = []
        actual = qy_factories.insert_into_qy(table, names)
        expected = 'INSERT INTO TABLE () VALUES ();'
        self.assertEqual(actual, expected)    
    
    def test_withNames_insert_into_qy(self):
        table = 'TABLE'
        names = ['col1', 'col2']
        actual = qy_factories.insert_into_qy(table, names)
        expected = 'INSERT INTO TABLE (col1,col2) VALUES (?,?);'
        self.assertEqual(actual, expected)    
    
    def test_emptyFields_create_db_qy(self):
        table = 'TABLE_NAME'
        fields = []
        actual = qy_factories.create_db_qy(table, fields)
        expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME ();'
        self.assertEqual(actual, expected)    
    
    def test_withOneField_create_db_qy(self):
        table = 'TABLE_NAME'
        fields = [{'name': 'col1', 'type': 'TYPE1'}]
        actual = qy_factories.create_db_qy(table, fields)
        expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME (col1 TYPE1);'
        self.assertEqual(actual, expected)    
    
    def test_withManyFields_create_db_qy(self):
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
        self.assertEqual(actual, expected)

    def test_select_table_name_from_db_qy(self):
        db = 'DB'
        tb = 'TB'
        actual = qy_factories.select_table_name_from_db_qy(db, tb)
        expected = "SELECT name FROM sqlite_master WHERE type='table' AND name='TB' LIMIT 1;"
        self.assertEqual(actual, expected)

    def test_count_nrows(self):
        actual = qy_factories.count_nrows("TB")
        expected = "SELECT Count(*) FROM TB;"
        self.assertEqual(actual, expected)

    def test_sum_col(self):
        actual = qy_factories.sum_col("TB", "COL")
        expected = "SELECT SUM(COL) FROM TB;"
        self.assertEqual(actual, expected)