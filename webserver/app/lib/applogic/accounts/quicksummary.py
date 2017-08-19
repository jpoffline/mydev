
from dumpable import DUMPABLE
import envelope_to_icon_map as envicon

class QuickSummary(DUMPABLE):
    def __init__(self, summary, total, mincount=0, maxcount=None):
        self._summary = summary
        self._total = total
        self._total_this = None
        self._data = None
        self._mincount = mincount
        self._dont_add = None
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

        if self._dont_add is None:
            self._find_dontadd()

        this_total = 0
        for item in self._summary:
            if item['meta']['count'] > self._mincount and item['name'] not in self._dont_add:
                returns.append(self._rows(item))
                this_total += item['meta']['total']
        self._data = returns
        self._total_this = this_total

    def _find_dontadd(self):
        dont_add = []
        for i in xrange(0, len(self._summary)):
            for j in xrange(i,len(self._summary)):
                if self._summary[i]['name'] == self._summary[j]['name']:
                    dont_add.append(self._summary[i]['name'])
                    break
        
        dd2 = dict((i, dont_add.count(i)) for i in dont_add)
        dont_add = []
        for k,v in dd2.iteritems():
            if v >1:
                dont_add.append(k)
        
        self._dont_add = dont_add

    def _generate_withmax(self, maxcount):
        returns = []
        this_total = 0
        names_in = []

        if self._dont_add is None:
            self._find_dontadd()
        

        for item in self._summary:
            if item['meta']['count'] <= maxcount:
                if item['name'] not in self._dont_add:
                    returns.append(self._rows(item))
                    this_total += item['meta']['total']
                    names_in.append(item['name'])

        #print returns
        
        self._data = returns
        self._total_this = this_total

    def data(self):
        return self._data

    def header(self):
        return self._header()

    def topn(self,n):
        return self._data[:n]