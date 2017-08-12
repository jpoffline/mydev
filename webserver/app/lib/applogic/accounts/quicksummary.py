
import csvhelp as csv

class QuickSummary(object):
    def __init__(self, summary, total):
        self._data = summary
        self._total = total
        self._qs = None
        self._generate()
        pass

    def _header(self):
        return ('name', 'total', 'count', 'frac')

    def _generate(self):
        returns = []
        for item in self._data:
            returns.append((
                item['name'],
                str(item['meta']['total']),
                str(item['meta']['count']),
                round(item['meta']['total'] / self._total * 100, 2)
            ))
        self._qs = returns

    def get(self):
        return self._qs

    def header(self):
        return self._header()

    def tocsv(self, filename):        
        csv.dump(filename, self.header(), self._qs)


