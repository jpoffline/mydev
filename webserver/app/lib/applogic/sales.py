
import app.lib.services.hostinfo as hostinfo
import app.lib.tools.tools as tools


class SalesData(object):
    def __init__(self):
        self._data = []

    def add(self, data):
        """ Add data to the sales """
        self._data.append(data)

    def get(self):
        """ Get the entire sales data """
        return self._data

    def get_sorted(self, key='id', desc=True):
        """ Get the sales, sorted on a particular key in the data """
        return sorted(self._data, key=lambda k: k[key], reverse=desc)

    def len(self):
        return len(self._data)


class Sales(object):
    def __init__(self):
        self._sales = SalesData()
        self._total_income = 0
        self._short_desc_length = 25
        self._transact_id = 0
        pass

    def _sanitise_desc(self, in_desc):
        """ Truncate the description """
        return tools.truncate_string(in_desc)

    def _sanitise_amount(self, amount):
        return float(amount)

    def _monetise_amount(self, amount):
        """ Turn a value string into GBP """
        return tools.append_gbp(amount)

    def add_sale(self, sale_info):
        """ Add a sale to the log """
        self._transact_id += 1
        amount = self._sanitise_amount(sale_info['amount'])
        description = sale_info['description']
        self._sales.add(
            {
                'id': self._transact_id,
                'date': hostinfo.get_datetime(pretty=True),
                'title': sale_info['title'],
                'description': self._sanitise_desc(description),
                'amount_disp': self._monetise_amount(amount),
                'amount': amount,
                'full_desc': description
            }
        )
        self._total_income += amount

    def get_sales(self):
        """ Get a meta-heavy copy of the sales data """
        return {
            'sales': self._sales.get_sorted(),
            'running_total': self._monetise_amount(self._total_income)
        }

    def get_nsales(self):
        """ Get the current number of sales """
        return self._sales.len()