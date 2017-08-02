# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app


import app.lib.applogic.sales as sales


class ServiceTestSales(unittest.TestCase):

    def setUp(self):
        self._dummy_username = 'USERNAME'
        self.sales = sales.Sales()

    def tearDown(self):
        self.sales.delete_users_sales_record(doit=True)
        pass

    def test_bootup(self):
        actual = self.sales.get_sales()
        expected = {
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
        self.assertEqual(actual, expected)
        self.assertEqual(self.sales.get_totalsales(), 0)
        self.assertEqual(self.sales.get_average_sale(), 'NA')
        self.assertEqual(self.sales.loggedin(), False)

    def test_logUserIn(self):
        self.assertEqual(self.sales.loggedin(), False)
        self.sales.log_user_in(self._dummy_username)
        self.assertEqual(self.sales.loggedin(), True)

    def test_addSales(self):
        self.assertEqual(self.sales.loggedin(), False)
        self.sales.log_user_in(self._dummy_username)
        self.assertEqual(self.sales.loggedin(), True)

        dummy_sale = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': 'NOW',
            'submit_machine': 'TOY'
        }

        dummy_sale2 = {
            'amount': 12.21,
            'description': 'DESC2',
            'user': self._dummy_username,
            'title': 'TITLE2',
            'datetime': 'NOW2',
            'submit_machine': 'TOY'
        }

        self.sales.add_sale(dummy_sale)
        self.assertEqual(self.sales.get_nsales(), 1)
        self.sales.add_sale(dummy_sale2)

        expected_sales = {
            'average': 12.21,
            'running_total': 24.42,
            'sales': [
                {'description': u'DESC2',
                 'title': u'TITLE2',
                 'amount': 12.21,
                 'date': u'NOW2',
                 'full_desc': u'DESC2',
                 'id': 2
                 },
                {'description': u'DESC',
                 'title': u'TITLE',
                 'amount': 12.21,
                 'date': u'NOW',
                 'full_desc': u'DESC',
                 'id': 1
                 }

            ]
        }

        self.assertEqual(self.sales.get_sales(), expected_sales)
        self.assertEqual(self.sales.get_nsales(), 2)
        #self.assertEqual(self.sales._sales.getall(), False)

    def test_distinctDates(self):
        self.assertEqual(self.sales.loggedin(), False)
        self.sales.log_user_in(self._dummy_username)
        self.assertEqual(self.sales.loggedin(), True)

        dummy_sale = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': '2017-05-01',
            'submit_machine': 'TOY'
        }
        self.sales.add_sale(dummy_sale)

        self.assertEqual(self.sales.get_nsales(), 1)
        self.assertEqual(self.sales._sales.get_distinct_dates(), ['2017-05'])

        dummy_sale2 = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': '2017-04-01',
            'submit_machine': 'TOY'
        }
        self.sales.add_sale(dummy_sale2)
        self.assertEqual(self.sales.get_nsales(), 2)
        self.assertEqual(self.sales._sales.get_distinct_dates(), [
                         '2017-04', '2017-05'])

        dummy_sale3 = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': '2012-04-01',
            'submit_machine': 'TOY'
        }
        self.sales.add_sale(dummy_sale3)

        self.assertEqual(self.sales.get_nsales(), 3)
        self.assertEqual(self.sales._sales.get_distinct_dates(), [
                         '2012-04', '2017-04', '2017-05'])

    def sanity_digit(self, digit):
        if digit > 9:
            return str(digit)
        return '0' + str(digit)

    def crank_and_add_sale_over_datetime(self, saleMeta):
        for month in xrange(1, 5):
            month = self.sanity_digit(month)
            for day in xrange(1, 6):
                for hour in xrange(0, 5):
                    saleMeta['datetime'] = '2012-' + month + '-' + \
                        self.sanity_digit(day) + ' ' + \
                        self.sanity_digit(hour) + ':21:31'
                    self.sales.add_sale(saleMeta)

    def test_GetDataInDate_distinctDates(self):
        self.assertEqual(self.sales.loggedin(), False)
        self.sales.log_user_in(self._dummy_username)
        self.assertEqual(self.sales.loggedin(), True)
        dummy_sale3 = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': '2012-04-01',
            'submit_machine': 'TOY'
        }
        self.sales.add_sale(dummy_sale3)

        self.assertEqual(self.sales.get_nsales(), 1)

        self.crank_and_add_sale_over_datetime(dummy_sale3)

        ss = self.sales._sales.get_sales_for_date('2012-02', agglevel='month')
        self.assertEqual(len(ss['amounts']), 5)
        self.assertEqual(len(ss['counts']), 5)
        self.assertEqual(len(ss['dates']), 5)
        self.assertEqual(ss['dates'], ['01','02', '03', '04','05'])

    def test_GetAllDataForTime_distinctDates(self):
        self.assertEqual(self.sales.loggedin(), False)
        self.sales.log_user_in(self._dummy_username)
        self.assertEqual(self.sales.loggedin(), True)
        dummy_sale3 = {
            'amount': 12.21,
            'description': 'DESC',
            'user': self._dummy_username,
            'title': 'TITLE',
            'datetime': '2012-04-01',
            'submit_machine': 'TOY'
        }
        self.sales.add_sale(dummy_sale3)
        self.crank_and_add_sale_over_datetime(dummy_sale3)

        ss = self.sales._sales.get_agg_sales_for_all_dates()
        self.assertEqual(len(ss), 4)
        for item in ss:
            self.assertEqual(len(item['sales']['amounts']), 5)
            self.assertEqual(len(item['sales']['counts']), 5)
            self.assertEqual(len(item['sales']['dates']), 5)
