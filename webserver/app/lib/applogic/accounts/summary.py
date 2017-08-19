
import quicksummary as quicksummary
import summaryoverview as summaryoverview
import accountreport as accountreport
import reccurences as reccurences

class SummariseByDescription(object):
    def __init__(self, printer, accounts, meta={}):
        self._accounts = accounts
        self._print = printer
        self._summary = self._gen_summaries()
        self._meta = meta

    def _gen_summary(self, data, which, row):

        if row.period in data:
            if row.description in data[row.period]:
                data[row.period][row.description]['total'] += row.get(which)
                data[row.period][row.description]['count'] += 1
                data[row.period][row.description]['transactions'].append(
                    (row.date, row.get(which)))
            else:
                data[row.period][row.description] = {}
                data[row.period][row.description]['total'] = row.get(which)
                data[row.period][row.description]['count'] = 1
                data[row.period][row.description]['period'] = row.period
                data[row.period][row.description]['group'] = row.group
                data[row.period][row.description]['transactions'] = [
                    (row.date, row.get(which))]
        else:
            data[row.period] = {}
            return self._gen_summary(data, which, row)
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

    def quick_summary(self, summary, total, mincount=0, maxcount=None):
        return quicksummary.QuickSummary(summary, total, mincount=mincount, maxcount=maxcount)

    def _clean_summary(self, summary):
        items = []
        for kk, sum_period in summary.iteritems():
            for k, v in sum_period.iteritems():
                items.append({'name': k, 'meta': v})
            # Sort summary items on the total
            items = sorted(items, key=lambda k: k['meta']['total'], reverse=True)
        return items

    def _find_recurring_all_periods(self, data):
        periods = data.keys()
        if len(periods) == 1: 
            return []
        periods.reverse()
        recurring = []
        for item, v in data[periods[0]].iteritems():
            itsin = True
            store = [data[periods[0]][item]]
            for i in xrange(1,len(periods)):
                if item not in data[periods[i]].keys():
                    itsin = False
                    break
                store.append(data[periods[i]][item])
            if itsin:
                recurring.append({'name':item,'store':store})
        recurring_items = {
            'periods': periods,
            'recurring_items':recurring
        }


        return recurring_items



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
            'count_items': self._accounts.counts(),
            'period': self._accounts.period(),
            'balance': self._accounts.balance_open_close(),
            'recurring_credits':reccurences.reccurences(summary_credit),
            'recurring_debits':reccurences.reccurences(summary_debit)
        }

    def save_overview(self, filename=None):
        summaryoverview.SummaryOverview(self._summary).to_csv(filename)

    def create_summariesSave(self, meta,tocsv=False):

        summary_credit = self._summary['credits']
        summary_debit = self._summary['debits']

        clean_credit = self._clean_summary(summary_credit)
        clean_debit = self._clean_summary(summary_debit)

        qs_debit = self.quick_summary(
            clean_debit, self._accounts.total_debit())
        qs_credit = self.quick_summary(
            clean_credit, self._accounts.total_credit())


        summary_debit_min = self.quick_summary(
            clean_debit, self._accounts.total_debit(), mincount=1)
        summary_debit_max = self.quick_summary(
            clean_debit, self._accounts.total_debit(), maxcount=1)

        summary_credit_min = self.quick_summary(
            clean_credit, self._accounts.total_credit(), mincount=1)
        summary_credit_max = self.quick_summary(
            clean_credit, self._accounts.total_credit(), maxcount=1)



        report_meta = {
            'report_debit_regular': summary_debit_min.to_html_table(),
            'report_credit_regular': summary_credit_min.to_html_table(),
            'report_debit_oneoff': summary_debit_max.to_html_table(),
            'report_credit_oneoff': summary_credit_max.to_html_table(),
            'period': self._summary['period'],
            'total_debit': str(self._summary['total_debit']),
            'total_credit': str(self._summary['total_credit']),
            'balance': self._summary['balance'],
            'recurring_credits': self._summary['recurring_credits'].to_html_table(),
            'recurring_debits': self._summary['recurring_debits'].to_html_table(),
            'count_items': self._summary['count_items'],
            'top5_oneoff_debit':summary_debit_max.to_html_table(topn=5),
            'top5_oneoff_debit_pie':summary_debit_max.to_plot_pie({'values':2,'labels':0,'labels2':(4,'% of all debits')}),
            'meta': self._meta
        }

        if tocsv:
            qs_debit.to_csv(meta['summary-debit'])
            qs_credit.to_csv(meta['summary-credit'])
            summary_debit_min.to_csv(meta['summary-regular-debit'])
            summary_debit_max.to_csv(meta['summary-oneoff-debit'])
            summary_credit_min.to_csv(meta['summary-regular-credit'])
            summary_credit_max.to_csv(meta['summary-oneoff-credit'])

        accountreport.accountreport(meta['summary-html'], report_meta).to_file(meta['summary-html'])
