
import quicksummary as quicksummary
import summaryoverview as summaryoverview


class SummariseByDescription(object):
    def __init__(self, printer, accounts):
        self._accounts = accounts
        self._print = printer
        self._summary = self._gen_summaries()

    def _gen_summary(self, data, which, row):
        if row.description in data:
            data[row.description]['total'] += row.get(which)
            data[row.description]['count'] += 1
            data[row.description]['transactions'].append(
                (row.date, row.get(which)))
        else:
            data[row.description] = {}
            data[row.description]['total'] = row.get(which)
            data[row.description]['count'] = 1
            data[row.description]['transactions'] = [
                (row.date, row.get(which))]
        return data

    def find_max_amount_group(self, group):
        max_total = {'total': 0}
        for k, v in group.iteritems():
            if v['total'] > max_total['total']:
                name, max_total = k, group[k]
        return {'who': name, 'data': max_total}

    def _print_item_summary(self, k, v, total, opts):
        self._print.write(k)
        self._print.write('  Number ' + str(v['count']))
        self._print.write('  Amount ' + str(v['total']) + ' : ' + str(
            round(v['total'] / total * 100, 2)) + '% of total')
        if v['total'] > 1 and opts.get('print_transactions', False):
            self._print.write('  Transactions')
            for item in v['transactions']:
                self._print.write(
                    '     Date ' + item[0] + ' : ' + str(item[1]))

    def print_summary(self, summary, total, opts):
        for k in summary:
            self._print_item_summary(k['name'], k['meta'], total, opts)

    def quick_summary(self, summary, total, mincount=0,maxcount=None):
        return quicksummary.QuickSummary(summary, total, mincount=mincount,maxcount=maxcount)

    def _clean_summary(self, summary):
        items = []
        for k, v in summary.iteritems():
            items.append({'name': k, 'meta': v})
        # Sort summary items on the total
        items = sorted(items, key=lambda k: k['meta']['total'])
        return items

    def _gen_summaries(self):
        summary_credit = {}
        summary_debit = {}
        for row in self._accounts.rows():
            if row.credit > 0:
                summary_credit = self._gen_summary(
                    summary_credit, 'credit', row)
            if row.debit > 0:
                summary_debit = self._gen_summary(
                    summary_debit, 'debit', row)

        return {
            'credits': summary_credit,
            'debits': summary_debit,
            'total_debit': self._accounts.total_debit(),
            'total_credit': self._accounts.total_credit(),
            'period': self._accounts.period()
        }

    def save_summaryOverview(self, filename=None):
        summaryoverview.SummaryOverview(self._summary).to_csv(filename)

    def create_summariesSave(self, meta):

        summary_credit = self._summary['credits']
        summary_debit = self._summary['debits']
        #print 'MAX', self.find_max_amount_group(summary_credit)
        #summaryoverview.SummaryOverview(summary).tocsv(config.SCRATCH + 'overview.csv')
        #print 'MAX', self.find_max_amount_group(summary_debit)
        #print summary_debit
        #print summary_credit
        clean_credit = self._clean_summary(summary_credit)
        clean_debit = self._clean_summary(summary_debit)
        #self.print_summary(clean_credit, self._accounts.total_credit(), {})
        #self.print_summary(clean_debit, self._accounts.total_debit(), {
        #                   'print_transactions': True})
        qs_debit = self.quick_summary(
            clean_debit, self._accounts.total_debit())
        qs_credit = self.quick_summary(
            clean_credit, self._accounts.total_credit())
        qs_debit.to_csv(meta['summary-debit'])
        qs_credit.to_csv(meta['summary-credit'])

        qs_debit = self.quick_summary(
            clean_debit, self._accounts.total_debit(), mincount=1).to_csv(meta['summary-regular-debit'])
        qs_credit = self.quick_summary(
            clean_credit, self._accounts.total_credit(), mincount=1).to_csv(meta['summary-regular-credit'])
        
        qs_debit = self.quick_summary(
            clean_debit, self._accounts.total_debit(), maxcount=1).to_csv(meta['summary-oneoff-debit'])
        qs_credit = self.quick_summary(
            clean_credit, self._accounts.total_credit(), maxcount=1).to_csv(meta['summary-oneoff-credit'])
        
        
