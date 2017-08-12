

class Transaction(object):
    #
    # Transaction Date
    # Transaction Type
    # Sort Code
    # Account Number
    # Transaction Description
    # Debit Amount
    # Credit Amount
    # Balance
    #
    def __init__(self, id, row):
        self.id = id
        self.row = row
        self.date = row[0]
        self.type = row[1]
        self.sortcode = row[2]
        self.accountnumber = row[3]
        self.description = row[4]
        self.debit = self.sanitise(row[5])
        self.credit = self.sanitise(row[6])
        self.balance = self.sanitise(row[7])
        self.group = None
        self.period = None

    def get(self, key):
        if key == 'credit':
            return self.credit
        elif key == 'debit':
            return self.debit
        else:
            return False

    def set_group(self, grp):
        self.group = grp

    def set_period(self, prd):
        self.period = prd
        #self.description += "-"+ prd

    def add(self, row):
        pass

    def sanitise(self, value):
        if value == '':
            return 0
        return float(value)

    def good(self):
        return True


from datetime import datetime


class Accounts(object):

    def __init__(self, mappings={}):
        self._rows = []
        self._count = 0
        self._recalc = True
        self._total_debit = None
        self._total_credit = None
        self._period_begin = datetime.today()
        self._period_end = datetime.strptime("01/01/1900", "%d/%m/%Y")
        self._descmappings = mappings['desc_maps']
        self._envelopemappings = mappings['envelope_maps']
        self._distinct_periods = []
        
        pass

    def _check_transact_desc(self, description):
        # Map the transaction description
        # if possible.
        return self._descmappings.get(
            description, description)

    def _check_transact_env(self, desc):
        for k, v in self._envelopemappings.iteritems():
            if desc in v:
                return k
        return ''

    def _check_transact_date(self, date):
        # Check the transaction date
        # to find the earliest
        # and latest dates.
        date = datetime.strptime(date, "%d/%m/%y")
        if date < self._period_begin:
            self._period_begin = date
        if date > self._period_end:
            self._period_end = date

        # Now see if the period has been seen before
        date_mmyy = date.strftime("%m-%y")
        if date_mmyy not in self._distinct_periods:
            self._distinct_periods.append(date_mmyy)
        return date_mmyy

    def _add_transaction(self, transaction):
        orig_desc = transaction.description
        transaction.description = self._check_transact_desc(orig_desc)
        transaction.set_group(self._check_transact_env(orig_desc))
        period = self._check_transact_date(transaction.date)
        transaction.set_period(period)
        
        self._rows.append(transaction)
        self._count += 1
        self._recalc = True
        

    def add_transaction(self, transaction):
        transaction = Transaction(self._count, transaction)
        if transaction.good():
            self._add_transaction(transaction)

    def rows(self):
        return self._rows

    def _calc_totals(self):
        if self._recalc:
            debit = 0
            credit = 0
            for row in self._rows:
                debit += row.debit
                credit += row.credit
            self._total_debit = round(debit, 2)
            self._total_credit = round(credit, 2)
            self._recalc = False

    def total_debit(self):
        self._calc_totals()
        return self._total_debit

    def total_credit(self):
        self._calc_totals()
        return self._total_credit

    def period(self):
        return{
            'begin': self._period_begin.strftime("%d/%m/%Y"),
            'end': self._period_end.strftime("%d/%m/%Y")
        }


class AccountsFile(object):
    def __init__(self, filename, mappings=None):
        self._filename = filename
        self._accounts = Accounts(mappings=mappings)
        self._readfile()

    def _readfile(self):
        import csv
        reader = csv.reader(open(self._filename, 'rU'), dialect=csv.excel_tab)
        data = [row for row in reader]
        for trans in data[1:]:
            self._accounts.add_transaction(trans[0].split(','))

    def stats(self):
        print 'Total credit', self._accounts.total_credit()
        print 'Total debit', self._accounts.total_debit()
        print 'N rows     ', len(self._accounts._rows)
