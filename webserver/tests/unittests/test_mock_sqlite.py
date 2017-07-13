# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app

import app.lib.sqlite.inmemory.database as mock_sqlite
from app.lib.tools.generalreturn import *


class TestMockSqlite(unittest.TestCase):

    def setUp(self):
        self.MOCK_tb_fields = [
            {'name': 'id', 'type': 'integer primary key'},
            {'name': 'person', 'type': 'text'},
            {'name': 'age', 'type': 'integer'}
        ]



        self.MOCK_db_name = 'PATH'
        self.MOCK_tb_name = 'TABLE'
        self.MOCK_insert_data = {
            'cols': ['person', 'age'],
            'data': [
                ('jonny', 29), ('iona', 26), ('thingy', 12)
            ]
        }

    def test_createTB_inmemorydb(self):
        table_fields = self.MOCK_tb_fields
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)

        self.assertEqual(sql.nrows(table), 0)
        self.assertEqual(sql.ntables(), 1)
        self.assertEqual(sql.ncols(table), 3)
        self.assertEqual(sql.get_path(), path)

    def test_createTBOtherPK_inmemorydb(self):
        table_fields = [
            {'name': 'id', 'type': 'integer'},
            {'name': 'person', 'type': 'integer primary key'},
            {'name': 'age', 'type': 'integer'}
        ]
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)
        
        self.assertEqual(sql.nrows(table), 0)
        self.assertEqual(sql.ntables(), 1)
        self.assertEqual(sql.ncols(table), 3)
        self.assertEqual(sql.get_path(), path)

    def test_createTBnoPK_inmemorydb(self):
        table_fields = [
            {'name': 'id', 'type': 'integer'},
            {'name': 'person', 'type': 'integer'},
            {'name': 'age', 'type': 'integer'}
        ]
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)
        
        self.assertEqual(sql.check_pk(table), False)
        self.assertEqual(sql.nrows(table), 0)
        self.assertEqual(sql.ntables(), 1)
        self.assertEqual(sql.ncols(table), 3)
        self.assertEqual(sql.get_path(), path)

    def test_createTBAndAdd_inmemorydb(self):
        table_fields = self.MOCK_tb_fields
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)
        # Insert some data
        insert_ok = sql.insert_into(path, table, self.MOCK_insert_data)

        self.assertEqual(sql.nrows(table), 3)
        self.assertEqual(sql.ncols(table), 3)
        self.assertEqual(sql.ntables(), 1)
        self.assertEqual(sql.get_colnames(table), ['id', 'person', 'age'])
        self.assertTrue(sql.check_pk(table))
        self.assertTrue(insert_ok)


    def test_getAll_inmemorydb(self):
        table_fields = self.MOCK_tb_fields
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)
        sql.insert_into(path, table, self.MOCK_insert_data)
        actual = sql.get_all_from_sql(path, table)
        expected = [(1, u'jonny', 29), (2, u'iona', 26), (3, u'thingy', 12)]
        self.assertEqual(actual, expected)

    def test_badData_inmemorydb(self):
        table_fields = self.MOCK_tb_fields
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        insert_data = {
            'cols': ['person', 'age'],
            'data': [
                ('jonny', 29),
                ('iona', 26, 89),
                ('thingy', 12)
            ]
        }
        sql.create_db(path, table, table_fields)
        actual = sql.insert_into(path, table, insert_data)
        expected = generalreturn(
            'inmemorydb_tb ERROR<add_row>: unexpected number of elements')
        self.assertEqual(actual, expected)

    def test_delete_inmemorydb(self):
        table_fields = self.MOCK_tb_fields
        sql = mock_sqlite.inmemorydb()
        path = self.MOCK_db_name
        table = self.MOCK_tb_name
        sql.create_db(path, table, table_fields)
        sql.insert_into(path, table, self.MOCK_insert_data)
        sql.delete_database(path)
        self.assertEqual(sql.ntables(), 0)
