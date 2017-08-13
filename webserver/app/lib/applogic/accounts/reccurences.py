from dumpable import DUMPABLE

class reccurences(DUMPABLE):
    def __init__(self, data):
        self._data = data
        self._header = []
        self._rows = []
        self._reccur = None
        self._periods = None
        self._find_recurring_all_periods()
        pass

    def get(self):
        return self._reccur

    def _find_recurring_all_periods(self):
        periods = self._data.keys()
        if len(periods) == 1: 
            return []
        periods.reverse()
        self._periods = periods
        recurring = []
        for item, v in self._data[periods[0]].iteritems():
            itsin = True
            store = [self._data[periods[0]][item]]
            for i in xrange(1,len(periods)):
                if item not in self._data[periods[i]].keys():
                    itsin = False
                    break
                store.append(self._data[periods[i]][item])
            if itsin:
                recurring.append({'name':item,'store':store})

        recurring_items = {
            'periods': periods,
            'recurring_items':recurring
        }

        self._reccur = recurring_items
        self._gen_data()
        self._gen_header()


    def _gen_data(self):

        for item in self._reccur['recurring_items']:
            row = [item['name']]
            c = 1
            bench = 0
            for t in item['store']:
                row.append(t['total'])
                row.append(t['count'])
                if c > 1:
                    row.append(t['total'] - bench)
                    pctg = round((t['total'] - bench) / bench * 100,2)
                    pctg = str(pctg) + '%'
                    row.append(pctg)
                else:
                    bench = t['total']
                c += 1
            self._rows.append(row)

        
        

    def _gen_header(self):
        self._header = ['name']
        c = 1
        for p in self._periods:
            self._header.append(p)
            self._header.append('count')
            if c > 1:
                self._header.append('diff')
                self._header.append('pctg')
            c += 1

    def data(self):
        return self._rows

    def header(self):
        return self._header