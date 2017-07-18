
class SalesData(object):
    def __init__(self):
        self._data = []
        self._id = 0

    def add(self, data):
        """ Add data to the sales """
        self._id += 1
        data['id'] = self._id
        self._data.append(data)

    def get(self):
        """ Get the entire sales data """
        return self._data

    def get_sorted(self, key='id', desc=True):
        """ Get the sales, sorted on a particular key in the data """
        return sorted(self._data, key=lambda k: k[key], reverse=desc)

    def len(self):
        return len(self._data)

