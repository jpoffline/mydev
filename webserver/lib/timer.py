
import time


def pretty_time(input_time, sig=2):
    """
    Return a pretty-string version of
    an inputted time in seconds
    """
    units = 'secs'
    if input_time > 60:
        input_time = input_time / 60
        units = 'mins'
    return str(round(input_time, sig)) + ' ' + units


class Timer(object):
    """ Timer class """

    def __init__(self):
        self._start = None
        self._end = None
        self._elapsed_seconds = None
        self.reset()
        self._sig = 2
        self._laps = []
        self._laps_sorted = False

    def start(self):
        """ Start the timer """
        self._start = time.time()

    def sig(self, input_sig):
        """ Set the significant figures for output """
        self._sig = input_sig

    def end(self):
        """ End the timer """
        self._end = time.time()
        self._elapsed_seconds = round(self._end - self._start, self._sig)

    def save(self, lap_id, reset=False):
        """ Save the elapsed time under an ID """
        self._laps.append({'id': lap_id, 'elapsed': self.elapsed_seconds()})
        if reset:
            self.reset()

    def reset(self):
        """ Reset the timer """
        self._start = None
        self._end = None
        self._elapsed_seconds = None

    def elapsed(self):
        """ Return a pretty-string version of the elapsed time """
        return pretty_time(self._elapsed_seconds, self._sig)

    def elapsed_seconds(self):
        """ Return the elapsed time in seconds """
        return self._elapsed_seconds

    def laps(self, sort=True):
        """
        Return the saved laps.

        By default will send back the laps sorted by elapsed time.
        """
        if sort:
            self.sort_laps()
        return self._laps

    def sort_laps(self):
        """ Sort the laps """
        self._laps = sorted(self._laps, key=lambda k: k['elapsed'])
        self._laps_sorted = True

    def slowest(self, last_n=5):
        """ Return the slowest of all the laps """
        if self._laps_sorted:
            return self._laps[-last_n:]
        print "NEED TO SORT LAPS FIRST"
        return None

    def fastest(self, top_n=5):
        """ Return the fastest of all the laps """
        if self._laps_sorted:
            return self._laps[0:top_n]
        print "NEED TO SORT LAPS FIRST"
        return None

    def lap_stats(self):
        """ Lap stats """
        last_lap_idx = len(self._laps) - 1
        return{
            'fastest': self._laps[last_lap_idx],
            'slowest': self._laps[0],
            'diff': self._laps[last_lap_idx]['elapsed'] - self._laps[0]['elapsed']
        }
