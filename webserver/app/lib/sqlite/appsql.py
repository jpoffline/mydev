import app.lib.sqlite.sql as sql

class AppSQL(object):
    def __init__(self, user=None, database=None, table=None):
        self._user=user
        self._table = table
        self._db_path = database
        self._database = sql.SQL(database=self._db_path)
        self._create()

    def _schema(self):
        """ Method to be overriden by inheriting classes """
        pass

    def _insert_col_names(self):
        pass

    def delete_db(self, doit=False):
        if doit:
            import os
            try:
                os.remove(self._db_path)
            except OSError:
                pass

    def _retrieve(self, order='desc'):
        """ Internal method: retreive all data from SQL """
        ord = 'id ' + order
        # Get the schema
        schema = self._schema()
        # From the schema, construct a list of
        # column names
        what = [k['name'] for k in schema]
        return self._database.get_many(self._table, order=ord, what=what)

    def _create(self):
        """ Internal method: create the DB-TB """
        self._database.create_db(self._db_path,
                                 self._table,
                                 self._schema())
    
    def _insert(self, data):
        """ Internal method: insert data to SQL """

        insert_data = {
            'cols': self._insert_col_names(),
            'data': data
        }
        self._database.insert_many(self._table, insert_data)

    def getall(self):
        """ Get all """
        return self._retrieve()

    def getgeneral(self, query):
        """ Execute a particular query """
        return self._database.get_many_general(query)

    def sanitise(self, element):
        """ Sanitise an element to a string """
        if type(element) is int or float or long:
            return str(element)
        return element

    def all_to_bstable(self):
        """ Returns the contents of the SQL table as
        a bootstrap-format HTML-table """
        html = "<div class=\"table-responsive\">"
        table = "<table class=\"table table-striped table-hover\">"
        header = "<thead><tr>"
        for item in self._schema():
            header += "<th>" + item['name'] + "</th>"
        header += "</tr></thead>"
        body = "<tbody>"
        for row in self.getall():
            user_html = "<tr>"
            for element in row:
                user_html += "<td>" + self.sanitise(element) + "</td>"
            body += user_html + "</td>"
        body += "</tbody>"
        table += header + body + "</table>"
        html += table + "</div>"
        return html
