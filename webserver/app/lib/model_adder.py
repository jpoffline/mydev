""" model adder module """

import app.lib.sqlite.sqlite_api as sql
import app.lib.tools.tools as tools
import app.lib.widgets.htmlwidgets as htmlwidgets


class ModelAdder(object):
    """ The wrapper class for the adder functionality """
    def __init__(self):
        self._db_path = 'app/data/db/adder.db'
        self._table = 'history'
        self._user = tools.get_username()
        self._machine = tools.get_hostname()
        self._history = None

    def _db_history_fields(self, wanted='schema'):
        """ Definition of the fields for the history table """
        if wanted == 'schema':
            table_fields_schema = [
                {'name': 'id', 'type': 'INTEGER primary key'},
                {'name': 'a', 'type': 'NUMERIC'},
                {'name': 'b', 'type': 'NUMERIC'},
                {'name': 'submit_user', 'type': 'text'},
                {'name': 'submit_machine', 'type': 'text'},
                {'name': 'submit_time', 'type': 'text'}
            ]
            return table_fields_schema
        if wanted == 'col_names':
            return [
                'id',
                'a',
                'b',
                'submit_user',
                'submit_machine',
                'submit_time'
            ]
        if wanted == 'insert_col_names':
            return [
                'a',
                'b',
                'submit_user',
                'submit_machine',
                'submit_time'
            ]

    def _create_db(self):
        """ Create the SQL tables """
        sql.create_db(self._db_path, self._table, self._db_history_fields())

    def _insert(self, table, cols, data):
        """ Insert into the database """
        insert_data = {
            'cols': cols,
            'data': data
        }
        sql.insert_into(self._db_path, table, insert_data)

    def add_history_item(self, a, b):
        """ Interface: method to data into the history table. """
        hist_cols = self._db_history_fields('insert_col_names')
        hist_vals = [(a, b, self._user, self._machine, tools.get_datetime())]
        self._insert(self._table, hist_cols, hist_vals)

    def get_all_history(self):
        """ Get all contents of the history table; store in memory. """
        self._history = sql.get_all_from_sql(self._db_path, self._table, order='id desc')

    def serialise_history(self):
        """
        Serialise the history to HTML.

        Returns a HTML-table.
        """
        self.get_all_history()

        return htmlwidgets.datatable(self._db_history_fields('col_names'),
                                       self._history)

