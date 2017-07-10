
class mockSQLite_table(object):
    def __init__(self, table_name, fields):
        self._col_fields = fields
        self._col_names = None
        self._table_name = table_name
        self._rows = []
        self._has_pk = self._set_col_names()
        self._pk_count = 0
        pass

    def _set_col_names(self):
        self._col_names = [rec['name'] for rec in self._col_fields]
        return self._set_primary_key()

    def _set_primary_key(self):
        pk_idx = 0
        for rec in self._col_fields:
            if "primary key" in rec['type']:
                return pk_idx
            pk_idx += 1
        return False

    def check_pk(self):
        if self._has_pk is not False:
            return True
        return False

    def add_row(self, data):
        for row in data['data']:
            if self._has_pk is not False:
                dumm = list(row)
                dumm.insert(self._has_pk, self._pk_count)
                row = tuple(dumm)
                self._pk_count += 1
            self._rows.append(row)

    def ncols(self):
        """ Get the number of columns in the table """
        return len(self._col_names)

    def nrows(self):
        """ Get the number of rows in the table """
        return len(self._rows)

    def return_all(self):
        to_return = []
        for row in self._rows:
            to_return.append(
                {
                    'data' : [row],
                    'cols' : self._col_names
                }
            )
        return to_return
    def get_col_names(self):
        return self._col_names


class mockSQLite(object):
    def __init__(self):
        self._database={}
        self._tables=[]
        self._path = None
        pass

    def get_path(self):
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
        self._database.update({table:mockSQLite_table(table,fields)})
        self._tables.append(table)
        pass

    def insert_into(self, table, data):
        """ Insert data into the given table """
        self._database[table].add_row(data)
        pass

    def get_all_from_sql(self, path, table, order='id desc'):
        """ Get all data from the table """
        return self._database[table].return_all()

    def get_colnames(self, table):
        """ Get the column names of the table """
        return self._database[table].get_col_names()

    def check_pk(self, table):
        """ Check to see if the table has a primary key """
        return self._database[table].check_pk()