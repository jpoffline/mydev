import datetime


def get_datetime():
    """ Get the current datetime stamp in YYYYMMDDHHMMSS-form """
    today = datetime.datetime.today()
    return today.strftime('%d/%m/%Y %H:%M:%S')


class Sales(object):
    def __init__(self):
        self._sales = []
        self._total_income = 0
        self._short_desc_length = 25
        pass

    def _sanitise_desc(self, input):
        return (input[:25] + '...') if len(input) > 25 else input

    def _sanitise_amount(self, amount):
        return float(amount)

    def _monetise_amount(self, amount):
        return "%.2f" % amount

    def add_sale(self, title, desc, amount):
        amount = self._sanitise_amount(amount)
        self._sales.append(
            {
                'date': get_datetime(),
                'title': title,
                'description': self._sanitise_desc(desc),
                'amount_disp': self._monetise_amount(amount),
                'amount': amount,
                'full_desc': desc
            }
        )
        self._total_income += amount

    def get_sales(self):
        return {
            'sales': self._sales,
            'running_total': self._monetise_amount(self._total_income)
        }
