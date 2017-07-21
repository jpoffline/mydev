
from app.lib.sqlite.appsql import AppSQL
import app.config as config
import app.lib.services.hostinfo as hostinfo
import users_qyfacs as qyfacs

class UsersSQL(AppSQL):
    def __init__(self):
        super(UsersSQL, self).__init__(database=config.USERS_db, table=config.USERS_tb)

    def _schema(self):
        return [
                {'name': 'id', 'type': 'INTEGER primary key'},
                {'name': 'username', 'type': 'text'},
                {'name': 'realname', 'type': 'text'},
                {'name': 'regdate', 'type': 'text'},
                {'name': 'meta', 'type': 'text'}
            ]

    def _insert_col_names(self):
        """ The column names for inserting """
        return[
            'username', 'realname', 'regdate'
        ]

    def add(self, data):
        """
        Add data to the users.

        Expects a dict:
        data = {"username": <USERNAME>, "realname": <REALNAME>},
        and inserts this into the database along with the host
        date-time flag to denote when the user was added.
        """
        data = [(
            data['username'],
            data['realname'],
            hostinfo.get_datetime(pretty=True)
        )]
        self._insert(data)

    def get_distinct_usernames(self):
        """ Get a list of the distinct usernames """
        qy = qyfacs.select_distinct_username(self._table)
        res = self._database.get_many_general(qy)
        dist = []
        for re in res:
            dist.append(re[0])
        return dist

    def get_username_meta(self, user):
        qy = qyfacs.select_row_for_username(self._table, user)
        res = self._database.get_many_general(qy)
        meta = {
            'username': user,
            'realname': res[0][0],
            'regdate': res[0][1]
        }
        return meta