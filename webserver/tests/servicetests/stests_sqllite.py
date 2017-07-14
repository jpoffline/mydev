# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app


import app.lib.sqlite.sqlite_api as sql
from app.lib.tools.generalreturn import *


class ServiceTestSQLite(unittest.TestCase):

    def setUp(self):
        
        # Database which will be created in the setup,
        # and will be assumed to exist in the tests.
        self.MOCK_sql_database = 'tests/scratch/mysuper_exists.db'
        self.MOCK_sql_table = 'history'

        # Database which will be created during the tests.
        self.MOCK_CREATE_db = 'tests/scratch/mysuper.db'
        self.MOCK_CREATE_tb = 'mytable'

        self.MOCK_CREATE_fields = [
            {'name': 'id', 'type': 'integer primary key'},
            {'name': 'person', 'type': 'text'},
            {'name': 'age', 'type': 'integer'}
        ]

        # Name of a database which does not exist.
        self.MOCK_sql_database_not_exist = 'BAD_DATABASE'
        self.MOCK_sql_table_not_exist = 'BAD_TABLE'

        # Create some databases
        sql.create_db(
            self.MOCK_sql_database,
            self.MOCK_sql_table,
            self.MOCK_CREATE_fields)

    def tearDown(self):
        self.CLEANUP_service_sqlite(self.MOCK_sql_database)

    def CLEANUP_service_sqlite(self, db):
        if sql.delete_database(db):
            return True
        return False

    def test_FailOnDB_does_table_exist(self):
        actual = sql.does_table_exist(
            self.MOCK_sql_database_not_exist,
            self.MOCK_sql_table)
        expected = gret('No database')
        self.assertEqual(actual, expected)

    def test_does_table_exist(self):
        actual = sql.does_table_exist(
            self.MOCK_sql_database,
            self.MOCK_sql_table)
        expected = True
        self.assertEqual(actual, expected)

    def test_False_does_table_exist(self):
        actual = sql.does_table_exist(
            self.MOCK_sql_database,
            self.MOCK_sql_table_not_exist)
        expected = False
        self.assertEqual(actual, expected)

    def test_True_does_database_exist(self):
        actual = sql.does_database_exist(self.MOCK_sql_database)
        expected = True
        self.assertEqual(actual, expected)

    def test_False_does_database_exist(self):
        actual = sql.does_database_exist(self.MOCK_sql_database_not_exist)
        expected = False
        self.assertEqual(actual, expected)

    def test_createDB(self):

        sql.create_db(
            self.MOCK_CREATE_db,
            self.MOCK_CREATE_tb,
            self.MOCK_CREATE_fields)
        expected = True
        actual = sql.does_table_exist(self.MOCK_CREATE_db, self.MOCK_CREATE_tb)
        self.CLEANUP_service_sqlite(self.MOCK_CREATE_db)

        self.assertEqual(actual, expected)

    def test_check_sqlite_returns(self):

        sql.create_db(
            self.MOCK_CREATE_db,
            self.MOCK_CREATE_tb,
            self.MOCK_CREATE_fields)

        insert_data = {
            'cols': ['person', 'age'],
            'data': [
                ('jonny', 29), ('iona', 26), ('thingy', 12)
            ]
        }

        sql.insert_into(self.MOCK_CREATE_db, self.MOCK_CREATE_tb, insert_data)
        actual = sql.get_all_from_sql(self.MOCK_CREATE_db, self.MOCK_CREATE_tb)
        expected = [(1, u'jonny', 29), (2, u'iona', 26), (3, u'thingy', 12)]
        self.CLEANUP_service_sqlite(self.MOCK_CREATE_db)

        self.assertEqual(actual, expected)

    def test_throw_err(self):
        self.assertRaises(ValueError, sql.throw_sqlite_error, 'message')
