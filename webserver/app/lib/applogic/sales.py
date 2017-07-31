""" Module containing the sales class """

import app.lib.services.hostinfo as hostinfo
import app.lib.tools.tools as tools


import app.lib.applogic.salessql as salessql

import aux_sales.plotting as plotting


class Sales(object):
    """ The sales class """

    def __init__(self, user=None):
        self._username = user
        self._sales = None
        self._short_desc_length = 25
        self._cache_valid = False
        self._cached = None
        self._cache_nsales = None
        self._loggedin = False
        pass

    def _sanitise_desc(self, in_desc):
        """ Truncate the description """
        return tools.truncate_string(in_desc)

    def _sanitise_amount(self, amount):
        return float(amount)

    def _monetise_amount(self, amount):
        """ Turn a value string into GBP """
        return tools.append_gbp(amount)

    def _cache(self):
        if self.loggedin():
            sales = self._sales.get_sorted()
            total = self._sales.sum_amount()
            number = len(sales)
            if number > 0:
                average = round(total / number, 2)
            else:
                average = 'NA'
            self._cached = {
                'sales': sales,
                'running_total': total,
                'average': average
            }
            self._cache_nsales = number
            self._cache_valid = True
        else:
            self._cached = {
                'sales': [{
                    'id': '-',
                    'date': '-',
                    'title': '-',
                    'description': '-',
                    'amount': '-',
                    'full_desc': '-'
                }],
                'running_total': 0
            }
            self._cache_nsales = 0

    def _check_cache(self):
        if self._cache_valid is False:
            self._cache()

    def set_username(self, user):
        """ Set the username """
        self._username = user

    def add_sale(self, sale_info):
        """ Add a sale to the log """
        amount = self._sanitise_amount(sale_info['amount'])
        description = sale_info['description']
        self._sales.add(
            {
                'user': sale_info['user'],
                'date': hostinfo.get_datetime(pretty=True),
                'title': sale_info['title'],
                'description': self._sanitise_desc(description),
                'amount': amount,
                'full_desc': description
            },
            saletime=sale_info['datetime']
        )
        self._cache_valid = False

    def get_sales(self):
        """ Get a meta-heavy copy of the sales data """
        self._check_cache()
        return self._cached

    def get_nsales(self):
        """ Get the current number of sales """
        self._check_cache()
        return self._cache_nsales

    def get_totalsales(self):
        """ Get the total amount in sales """
        self._check_cache()
        return self._cached['running_total']

    def get_average_sale(self):
        self._check_cache()
        return self._cached['average']

    def plot_sales(self, agglevel='day'):
        """ Get a plot of the sales """
        return plotting.plot_sales(
            self._sales.get_amounts_plottable(agglevel=agglevel),
            meta={'agglevel': agglevel}
        )

    def loggedin(self):
        """ Returns whether or not the user
        has logged in yet """
        return self._loggedin

    def log_user_in(self, user):
        """ Log a user in """
        self.set_username(user)
        self._loggedin = True
        self._sales = salessql.SalesSQL(user)
        print 'Logged in', user
