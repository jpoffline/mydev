import sqlite3
import context
import os
import qy_factories as factories
from app.lib.tools.generalreturn import *


class SQL(object):
    def __init__(self, database=None):
        self._connection = None
        self._cursor = None
        self._database = database
        if self._database is not None:
            self.connect()
        pass
    
    def create_db(self, database, table, fields):
        """ Create a table in the database """
        c = self._connection.cursor()
        qy = factories.create_db_qy(table, fields)
        c.execute(qy)

    def connect(self, database=None):
        """ Connect to the database """
        if database is not None:
            self._database = database
        self._connection = sqlite3.connect(self._database)
        self._cursor = self._connection.cursor()

    def get_many(self, table, order=None, what=None):
        """ Wrapper to SELECT WHAT from the table """
        query = factories.get_all_from_sql_qy(table, order, what=what)
        return self._connection.execute(query).fetchall()

    def get_many_general(self, query):
        """ Wrapper to execute a general SQL query """
        return self._connection.execute(query).fetchall()

    def insert_many(self, table, data):
        """ Wrapper to insert many values into a table in the database """
        qy = factories.insert_into_qy(table, data['cols'])
        self._connection.executemany(qy, data['data'])
        self._connection.commit()

    def close(self):
        """ Close the SQL connection """
        self._connection.close()

    def count_nrows(self, table, where=None):
        """ return the number of rows in a given table """
        v = self._connection.execute(factories.count_nrows(table, where)).fetchall()
        return v[0][0]

    def sum_col(self, table, col, where=None):
        """ Sum the particular column in the table """
        v = self._connection.execute(factories.sum_col(table, col, where)).fetchall()
        return v[0][0]

    def select_groupby_time(self, table, meta, where=None):
        query = factories.select_groupby_time(table, meta, where)
        return self._connection.execute(query).fetchall()
