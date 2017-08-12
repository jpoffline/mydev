
from dumpable import DUMPABLE

class SummaryOverview(DUMPABLE):

    def __init__(self, summary):
        self._summary = summary
        self._data = None
        self._generate()

    def header(self):
        return ('ncreditors',
                'ndebitors',
                'total_debit',
                'total_credit',
                'period_begin',
                'period_end')

    def _generate(self):
        summary_credit = self._summary['credits']
        summary_debit = self._summary['debits']
        self._data = [(
            len(summary_credit.keys()),
            len(summary_debit.keys()),
            self._summary['total_debit'],
            self._summary['total_credit'],
            self._summary['period']['begin'],
            self._summary['period']['end']
        )]

    def data(self):
        return self._data

    