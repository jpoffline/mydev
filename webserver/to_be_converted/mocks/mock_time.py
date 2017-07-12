""" The mock time module """


class mock_time(object):
    """ A mock up of the python time class """
    def __init__(self):
        self._count = 0
        self._increment = 1

    def time(self):
        """
        Get the current time.

        Since this is a mock up, will
        also increment the internal clock.
        """
        prev = self._count
        self._count += self._increment
        return prev

    def set_increment(self, inc):
        """ Set the incrementer for the internal clock """
        self._increment = inc

    def cycle(self, ncycles):
        """
        Cycle the internal clock by a defined number of cycles.
        """
        self._count += ncycles * self._increment
