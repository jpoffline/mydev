import app.lib.sqlite.sql as sql

class AppSQL(object):
    def __init__(self, database=None, table=None):
        self._table = table
        self._db_path = database
        self._database = sql.SQL(database=self._db_path)
        self._create()

    def _schema(self):
        """ Method to be overriden by inheriting classes """
        pass

    def _insert_col_names(self):
        pass

    def _retrieve(self, order='desc'):
        """ Internal method: retreive all data from SQL """
        ord = 'id ' + order
        return self._database.get_many(self._table, order=ord)

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

    def all_to_bstable(self):
        html = "<div class=\"table-responsive\"><table class=\"table table-striped table-hover\">"
        header = "<thead><tr>"
        for item in self._schema():
            header += "<th>" + item['name'] + "</th>"
        header += "</tr></thead>"
        body = "<tbody>"
        for user in self.getall():
            user_html = "<tr>"
            for item in user:
                user_html += "<td>" + str(item) + "</td>"
            body += user_html + "</td>"
        body += "</tbody>"
        html += header + body + "</table></div>"
        return html
