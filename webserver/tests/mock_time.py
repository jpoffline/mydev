
class mock_time(object):
    def __init__(self):
        self._count = 0
        self._increment = 1
        pass

    def time(self):
        prev = self._count
        self._count += self._increment
        return prev

    def set_increment(self, inc):
        self._increment = inc

    def cycle(self, ncycles):
        self._count += ncycles*self._increment