
import csvhelp as csv

class QuickSummary(object):
    def __init__(self, summary, total, mincount=0,maxcount=None):
        self._summary = summary
        self._total = total
        self._data = None
        self._mincount = mincount
        if maxcount is None:
            self._generate_withmin()
        else:
            self._generate_withmax(maxcount)
        pass

    def _header(self):
        return ('name', 'total', 'count', 'frac')

    def _rows(self, item):
        return (item['name'],
                    str(item['meta']['total']),
                    str(item['meta']['count']),
                    round(item['meta']['total'] / self._total * 100, 2))

    def _generate_withmin(self):
        returns = []
        for item in self._summary:
            if item['meta']['count'] > self._mincount:
                returns.append(self._rows(item))
        self._data = returns

    def _generate_withmax(self, maxcount):
        returns = []
        for item in self._summary:
            if item['meta']['count'] <= maxcount:
                returns.append(self._rows(item))
        self._data = returns

    def get(self):
        return self._data

    def header(self):
        return self._header()

    def tocsv(self, filename):        
        csv.dump(filename, self.header(), self.get())


