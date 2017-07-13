
import context
from app.lib.tools.generalreturn import *
import app.lib.sqlite.inmemory.table as tb


class inmemorydb(object):
    """ An in-memory database class,
    with the same API as the sqlite database.
    """
    def __init__(self):
        self._database = {}
        self._tables = []
        self._path = None

    def get_path(self):
        """ Return the path for the database """
        return self._path

    def ntables(self):
        """ Find the number of tables in the database """
        return len(self._tables)

    def nrows(self, table):
        """ Find the number of rows in a given table """
        return self._database[table].nrows()

    def ncols(self, table):
        """ Find the number of columns in a given table """
        return self._database[table].ncols()

    def create_db(self, path, table, fields):
        """ Create a table in the database """
        self._path = path
        self._database.update({table: tb.inmemorydb_tb(table, fields)})
        self._tables.append(table)

    def delete_database(self, path):
        """ Delete the database """
        self._database = {}
        self._tables = []

    def insert_into(self, path, table, data):
        """ Insert data into the given table """
        return self._database[table].add_row(data)

    def get_all_from_sql(self, path, table, order='id desc'):
        """ Get all data from the table """
        return self._database[table].return_all()

    def get_colnames(self, table):
        """ Get the column names of the table """
        return self._database[table].get_col_names()

    def check_pk(self, table):
        """ Check to see if the table has a primary key """
        return self._database[table].check_pk()
