
class SingleUser(object):
    def __init__(self):
        self._username = None
        self._realname = None
        pass


class UsersDB(object):

    def __init__(self):
        self._users_meta = {}
        self._distinct_usernames = []
        self._users_loggedin = []

    def _add_user(self, meta):
        """ Checks to see if the current
        user has ever logged in before;
        if not, add their data to the DB.
        """
        username = meta['username']
        if username not in self._distinct_usernames:
            self._distinct_usernames.append(username)
            self._users_meta[username] = meta

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
        return self._distinct_usernames

    def get_loggedin_users(self):
        """ Get a list of the user names logged in """
        return self._users_loggedin

    def get_usersmeta_for_username(self, username):
        """ Get the users meta data for a given username """
        return self._users_meta[username]