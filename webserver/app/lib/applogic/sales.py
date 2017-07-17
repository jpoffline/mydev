
import app.lib.services.hostinfo as hostinfo
import app.lib.tools.tools as tools
import app.lib.sqlite.sqlite_api as sql

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

class SalesSQL(object):
    def __init__(self):
        self._database = sql
        self._table = 'sales'
        self._db_path = 'app/data/db/sales.db'
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
        self._database.create_db(self._db_path,
                                 self._table,
                                 self._schema())

    def _insert(self, data):
        insert_data = {
            'cols': self._insert_col_names(),
            'data': data
        }
        self._database.insert_into(self._db_path, self._table, insert_data)

    def _retrieve(self):
        return self._database.get_all_from_sql(
            self._db_path,
            self._table,
            order='id desc')

    
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


    def add(self, data):
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
        return self._database.count_nrows(self._db_path, self._table)

    def sum_amount(self):
        """ Return the sum of the amount column """
        return self._database.sum_col(self._db_path, self._table, 'amount')
        
        


class Sales(object):
    def __init__(self):
        #self._sales = SalesData()
        self._sales = SalesSQL()
        self._short_desc_length = 25
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

    def get_sales(self):
        """ Get a meta-heavy copy of the sales data """
        return {
            'sales': self._sales.get_sorted(),
            'running_total': self._monetise_amount(self._sales.sum_amount())
        }

    def get_nsales(self):
        """ Get the current number of sales """
        return self._sales.len()
