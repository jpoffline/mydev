
import app.lib.sqlite.sql as sql
import app.lib.services.hostinfo as hostinfo
import app.config as config

class SalesSQL(object):

    def __init__(self):
        
        self._table = config.SALES_tb
        self._db_path = config.SALES_db
        self._database = sql.SQL(database=self._db_path)
        self._create()
        pass

    def _schema(self):
        return [
                {'name': 'id', 'type': 'INTEGER primary key'},
                {'name': 'submit_user', 'type': 'text'},
                {'name': 'submit_machine', 'type': 'text'},
                {'name': 'submit_time', 'type': 'text'},
                {'name': 'title', 'type': 'text'},
                {'name': 'description', 'type': 'text'},
                {'name': 'full_desc', 'type': 'text'},
                {'name': 'amount', 'type': 'numeric'},
                {'name': 'amount_disp', 'type': 'text'}
            ]

    def _insert_col_names(self):
        return[
            'submit_user',
            'submit_machine',
            'submit_time',
            'title',
            'description',
            'full_desc',
            'amount',
            'amount_disp'
        ]

    def _create(self):
        """ Internal method: create the sales DB-TB """
        self._database.create_db(self._db_path,
                                 self._table,
                                 self._schema())

    def _insert(self, data):
        """ Internal method: insert sales data to SQL """
        insert_data = {
            'cols': self._insert_col_names(),
            'data': data
        }
        self._database.insert_many(self._table, insert_data)

    def _retrieve(self, order='desc'):
        """ Internal method: retreive all sales data from SQL """
        ord = 'id ' + order
        return self._database.get_many(self._table, order=ord)

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
                'amount_disp': item[8],
                'amount': item[7],
                'full_desc': item[6]
            })
        return to_plop

    def get_amounts_plottable(self):
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
        hourly = self.get_sales_byhour()
        results.update(hourly)
        return results

    def get_sales_byhour(self):
        """ Get the sales data, aggregated by the hour """
        meta = {}
        meta['timecol'] = 'submit_time'
        meta['fmt'] = '%Y-%m-%d %H'
        meta['others'] = "count(*), sum(amount)"
        data = self._database.select_groupby_time(self._table, meta)

        counts = []
        times = []
        sales = []
        for item in data:
            times.append(item[0])
            counts.append(item[1])
            sales.append(item[2])

        return {'counts': counts, 'times': times, 'sales': sales}

    def add(self, data):
        """ Add data to the sales """
        data = [(
            hostinfo.get_username(),
            hostinfo.get_hostname(),
            hostinfo.get_datetime(pretty=True),
            data['title'],
            data['description'],
            data['full_desc'],
            data['amount'],
            data['amount_disp']
        )]
        self._insert(data)

    def len(self):
        """ Return the number of rows """
        return self._database.count_nrows(self._table)

    def sum_amount(self):
        """ Return the sum of the amount column """
        return self._database.sum_col(self._table, 'amount')
        