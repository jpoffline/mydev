
import context
from app.lib.tools.generalreturn import *

class inmemorydb_tb(object):
    """ The in-memory class for a table
    in the in-memory database. """
    def __init__(self, table_name, fields):
        self._col_fields = fields
        self._table_name = table_name
        self._col_names, self._has_pk = self._set_col_names(self._col_fields)

        self._rows = []
        self._pk_count = 1
        pass

    def _set_col_names(self, col_fields):
        """ Internal method: set the column names,
        and check for the existence of a primary key.
        """
        return [rec['name'] for rec in col_fields], self._set_primary_key()

    def _set_primary_key(self):
        """ Internal method: set the primary key (if applicable) """
        pk_idx = 0
        for rec in self._col_fields:
            if "primary key" in rec['type']:
                return pk_idx
            pk_idx += 1
        return False

    def check_pk(self):
        """ Check to see if there is a primary key in the table.

        Return
        -------
        True if there is a primary key, and False if not.
        """
        if self._has_pk is not False:
            return True
        return False

    def add_row(self, data):
        """ Add data to the table """
        for row in data['data']:
            if self._has_pk is not False:
                dumm = list(row)
                dumm.insert(self._has_pk, self._pk_count)
                row = tuple(dumm)
                self._pk_count += 1
            if len(row) == self.ncols():
                self._rows.append(row)
            else:
                return generalreturn('inmemorydb_tb ERROR<add_row>: unexpected number of elements')
        return True

    def ncols(self):
        """ Get the number of columns in the table """
        return len(self._col_names)

    def nrows(self):
        """ Get the number of rows in the table """
        return len(self._rows)

    def return_all(self):
        """ Return all the data in the table """
        return self._rows

    def get_col_names(self):
        """ Get the column names in the table """
        return self._col_names


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
        self._database.update({table: inmemorydb_tb(table, fields)})
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
