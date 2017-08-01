from app.lib.sqlite.appsql import AppSQL
import app.lib.sqlite.sql as sql
import app.lib.services.hostinfo as hostinfo
import app.config as config
import app.lib.sqlite.qy_factories as qyfacs
import os

class SalesSQL(AppSQL):

    def __init__(self, user):
        db_path = config.SALES_db_root + user +'/'
        database = db_path + config.SALES_db_file
        hostinfo.check_and_create_path(db_path)


        super(SalesSQL, self).__init__(user=user,
                                       database=database,
                                       table=config.SALES_tb)
        self._username = user
        self._whereuser ='submit_user = ' + user
        pass

    def _schema(self):
        """ The table schema """
        return [
            {'name': 'id', 'type': 'INTEGER primary key'},
            {'name': 'submit_user', 'type': 'text'},
            {'name': 'submit_machine', 'type': 'text'},
            {'name': 'submit_time', 'type': 'text'},
            {'name': 'title', 'type': 'text'},
            {'name': 'description', 'type': 'text'},
            {'name': 'full_desc', 'type': 'text'},
            {'name': 'amount', 'type': 'numeric'}
        ]

    def _insert_col_names(self):
        """ On insertion, the ordering of the entries """
        return[
            'submit_user',
            'submit_machine',
            'submit_time',
            'title',
            'description',
            'full_desc',
            'amount'
        ]

    def get_sorted(self, key='id', desc=True):
        """ Get the sales, sorted on a particular key in the data """
        data = self._retrieve()
        to_plop = []
        for item in data:
            to_plop.append({
                'id': item[0],
                'date': item[3],
                'title': item[4],
                'description': item[5],
                'amount': item[7],
                'full_desc': item[6]
            })
        return to_plop

    def get_amounts_plottable(self,agglevel='hour'):
        """ Get the sales data in a plottable format """
        data = self._retrieve(order='asc')
        amount = []
        date = []
        id = []
        for item in data:
            amount.append(item[7])
            date.append(item[3])
            id.append(item[0])
        results = {'amount': amount, 'date': date, 'id': id}
        hourly = self.get_sales_aggregated(agglevel)
        results.update(hourly)
        return results

    def get_sales_aggregated(self,agglevel):
        """ Get the sales data, aggregated """
        meta = {}
        meta['timecol'] = 'submit_time'
        meta['fmt'] = qyfacs.agglevel_to_format(agglevel)
        meta['others'] = ["count(*)", "sum(amount)"]
        data = self._database.select_groupby_time(self._table, meta)

        counts = []
        times = []
        sales = []
        cumulative = []
        total = 0.0
        for item in data:
            times.append(item[0])
            counts.append(item[1])
            sales.append(item[2])
            total += item[2]
            cumulative.append(total)

        return {
            'counts': counts,
            'times': times,
            'sales': sales,
            'cumulative': cumulative}

    def add(self, data):
        """ Add data to the sales """
        data = [(
            data['user'],
            data['submit_machine'],
            data['date'],
            data['title'],
            data['description'],
            data['full_desc'],
            data['amount']
        )]
        self._insert(data)

    def len(self):
        """ Return the number of rows """
        return self._database.count_nrows(self._table)

    def sum_amount(self):
        """ Return the sum of the amount column """
        return self._database.sum_col(self._table, 'amount')

    def get_distinct_dates(self, agglevel='month'):
        meta = {}
        meta['fmt'] = qyfacs.agglevel_to_format(agglevel)
        meta['timecol'] = 'submit_time'
        qy = qyfacs.select_distinct_dates(self._table, meta)
        res = self._database.get_many_general(qy)
        dates = []
        for date in res:
            dates.append(date[0])
        return dates