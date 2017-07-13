
class generalreturn(object):
    def __init__(self, message=None, success=True):
        self._message = message
        if message is not None:
            success = False
        self._success = success
        
    def state(self):
        return self._success

    def message(self):
        return self._message

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def _serialise(self):
        return "<generalreturn\ message:%s success:%s>" % (self._message, self._success)

    def __repr__(self):
        return self._serialise()