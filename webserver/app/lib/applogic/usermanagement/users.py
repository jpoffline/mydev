

from userssql import UsersSQL


class UsersDB(object):

    def __init__(self):

        self._users_meta = {}
        self._distinct_usernames = []
        self._users_loggedin = []
        self._usersdb = UsersSQL()

    def _add_user(self, meta):
        """ Checks to see if the current
        user has ever logged in before;
        if not, add their data to the DB.
        """
        username = meta['username']
        if username not in self._usersdb.get_distinct_usernames():
            self._users_meta[username] = meta
            self._usersdb.add(meta)

    def _log_user_in(self, meta):
        """ Log a particular user in.
        Also adds the username to the
        list of distinct usernames, if
        its a new user.
        """
        self._add_user(meta)
        self._users_loggedin.append(meta)

    def log_user_in(self, meta):
        """ Register a particular user to the DB """
        self._log_user_in(meta)

    def get_usernames(self):
        """ Get a list of usernames """
        return self._usersdb.get_distinct_usernames()

    def get_loggedin_users(self):
        """ Get a list of the user names logged in """
        return self._users_loggedin

    def get_usersmeta_for_username(self, username):
        """ Get the users meta data for a given username """
        return self._usersdb.get_username_meta(username)

    def get_all_users_info(self):
        """ Get all data from the users table """
        return self._usersdb.getall()

    def user_to_table(self):
        """ Get the raw users data, return in a
        bootstrap-format table """
        return self._usersdb.all_to_bstable()

