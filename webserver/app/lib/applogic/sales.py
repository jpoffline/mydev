""" Module containing the sales class """

import app.lib.services.hostinfo as hostinfo
import app.lib.tools.tools as tools
import app.lib.applogic.salessql as salessql
import aux_sales.plotting as plotting
import app.lib.widgets.bswidgets as bswidgets


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
                'running_total': 0,
                'average': 'NA'
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
                'date': sale_info.get('datetime', hostinfo.get_datetime(pretty=True)),
                'title': sale_info['title'],
                'description': self._sanitise_desc(description),
                'amount': amount,
                'full_desc': description,
                'submit_machine': sale_info.get('submit_machine', hostinfo.get_hostname())
            }
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

    def agg_sales_stats(self, data):
        """ Generate a text string per
        item for the sales data """
        mean = sum(data['sales']) / len(data['sales'])
        maxdata = max(data['sales'])
        meta = []
        for idx, point in enumerate(data['sales']):
            dev = round(point - mean, 2)
            frc = round(point / mean, 2)
            fmx = round(point / maxdata * 100, 2)
            text = data['times'][idx] + "<br>" + \
                'Number of sales: ' + str(data['counts'][idx]) + '<br>' + \
                'Deviation from average: ' + str(dev) + '<br>' +\
                'Fraction of average: ' + str(frc) + '%' + '<br>' +\
                'Fraction of maximum: ' + str(fmx) + '%''<br>'
            meta.append(text)
        return meta

    def plot_sales(self, agglevel='day'):
        """ Get a plot of the sales """
        data = self._sales.get_amounts_plottable(agglevel=agglevel)
        text = ['Number of sales: ' + str(d) for d in data['counts']]
        text = self.agg_sales_stats(data)
        plot = plotting.plot_box(
            {
                'x': data['times'],
                'y': data['sales'],
                'text': text
            },
            meta={'title': 'Sales by ' + agglevel}
        )

        return bswidgets.inWell().get(plot)

    def compare_sales(self):
        comparison_data = self._sales.get_agg_sales_for_all_dates()
        for data in comparison_data:
            date = data['date']
            amounts = data['sales']['amounts']
            counts = data['sales']['counts']
            days = data['sales']['dates']



    def loggedin(self):
        """ Returns whether or not the user
        has logged in yet """
        return self._loggedin

    def log_user_in(self, user):
        """ Log a user in """
        self.set_username(user)
        self._loggedin = True
        self._sales = salessql.SalesSQL(user)

    def delete_users_sales_record(self, doit=False):
        """ Delete a users sales record.
        Will delete the SQLite db file """
        if self.loggedin():
            self._sales.delete_db(doit=doit)
