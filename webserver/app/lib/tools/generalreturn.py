""" General return module """


class gret(object):
    """ Useful general return object """

    def __init__(self, message=None):
        self._message = message
        if message is not None:
            self._success = False
        else:
            self._success = True

    def state(self):
        """ Return the state of the return """
        return self._success

    def message(self):
        """ Return the message associated with the return object """
        return self._message

    def __eq__(self, other):
        """ Define equality between two gret's """
        return self.__dict__ == other.__dict__

    def _serialise(self):
        """ Serialise a given gret object """
        return "<generalreturn\ message:%s success:%s>" % (self._message, self._success)

    def __repr__(self):
        """ Define the print method for a gret object """
        return self._serialise()