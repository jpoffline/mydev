
import app.lib.services.hostinfo as hostinfo
import app.lib.tools.tools as tools


import app.lib.applogic.salessql as salessql

import plotly
import plotly.graph_objs as go

class Sales(object):
    def __init__(self):
        self._sales = salessql.SalesSQL()
        self._short_desc_length = 25
        self._cache_valid = False
        self._cached = None
        self._cache_nsales = None
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
        self._cached = {
            'sales': self._sales.get_sorted(),
            'running_total': self._monetise_amount(self._sales.sum_amount())
        }
        self._cache_nsales = len(self._cached['sales'])
        self._cache_valid = True

    def _check_cache(self):
        if self._cache_valid is False:
            self._cache()

    def add_sale(self, sale_info):
        """ Add a sale to the log """
        amount = self._sanitise_amount(sale_info['amount'])
        description = sale_info['description']
        self._sales.add(
            {
                'date': hostinfo.get_datetime(pretty=True),
                'title': sale_info['title'],
                'description': self._sanitise_desc(description),
                'amount_disp': self._monetise_amount(amount),
                'amount': amount,
                'full_desc': description
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

    def plot_sales(self):
        """ Get a plot of the sales """
        sales_data = self._sales.get_amounts_plottable()
        graph = {
            "data": [go.Scatter(x=sales_data['date'], y=sales_data['amount'])],
            "layout": go.Layout(
                title="Sales",
                xaxis={'title': 'Date'},
                yaxis={'title': 'Amount'}
            )
        }
        div = plotly.offline.plot(graph,
                                  show_link=False,
                                  output_type="div",
                                  include_plotlyjs=False)

        return div

