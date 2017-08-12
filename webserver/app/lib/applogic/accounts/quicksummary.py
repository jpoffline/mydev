
from dumpable import DUMPABLE
import envelope_to_icon_map as envicon

class QuickSummary(DUMPABLE):
    def __init__(self, summary, total, mincount=0, maxcount=None):
        self._summary = summary
        self._total = total
        self._total_this = None
        self._data = None
        self._mincount = mincount
        if maxcount is None:
            self._generate_withmin()
        else:
            self._generate_withmax(maxcount)
        self._consolidate()
        pass

    def _header(self):
        return ('name', 'period','total', 'count', 'frac_global', 'frac_group', 'envelope')

    def _rows(self, item):
        return (item['name'],
                item['meta']['period'],
                round(item['meta']['total'], 2),
                item['meta']['count'],
                round(item['meta']['total'] / self._total * 100, 2), 
                0, 
                envicon.env_to_icon_mapper(item['meta']['group']))

    def _consolidate(self):
        for row in xrange(0, len(self._data)):
            tmp = list(self._data[row])
            tmp[5] = round(tmp[2] / self._total_this * 100, 2)
            self._data[row] = tuple(tmp)

    def _generate_withmin(self):
        returns = []
        this_total = 0
        for item in self._summary:
            if item['meta']['count'] > self._mincount:
                returns.append(self._rows(item))
                this_total += item['meta']['total']
        self._data = returns
        self._total_this = this_total

    def _generate_withmax(self, maxcount):
        returns = []
        this_total = 0
        for item in self._summary:
            if item['meta']['count'] <= maxcount:
                returns.append(self._rows(item))
                this_total += item['meta']['total']
        self._data = returns
        self._total_this = this_total

    def data(self):
        return self._data

    def header(self):
        return self._header()
