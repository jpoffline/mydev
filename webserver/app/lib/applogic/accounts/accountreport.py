
from dumpable import DUMPABLE
import app.lib.widgets.bswidgets as bswidgets
import html_report as html_report
import datetime as datetime


class accountreport(DUMPABLE):
    def __init__(self, filename, meta):
        self._filename = filename
        self._meta = meta

    def content(self):

        nice_new_report = html_report.htmlreport({
            'update': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'meta': self._meta['meta']
        })

        nice_new_report._snav.add_top_collection({
            'name': 'Accounts',
            'icon': 'calculator'
        }
        )

        for page in self._meta['link_pages']:
            nice_new_report._snav.add_top_item_to_collection(
                'Accounts',
                page
            )


        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Top 5 one-off debits',
                'content': self._meta['top5_oneoff_debit'],
                'id': 'top5_oneoff_debit',
                'menugroup': 'Credits'
            }
        )

        nice_new_report.add_side_nav_item(
            {
                'title': 'Top 5 one-off debits',
                'link': 'top5_oneoff_debit',
                'icon': 'wrench'
            }
        )

        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Credits: recurring',
                'content': self._meta['recurring_credits'],
                'id': 'recurring_credits',
                'menugroup': 'Credits'
            }
        )
        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Credits: multiple',
                'content': self._meta['report_credit_regular'],
                'id': 'report_credit_regular',
                'menugroup': 'Credits'
            }
        )
        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Credits: one-offs',
                'content': self._meta['report_credit_oneoff'],
                'id': 'report_credit_oneoff',
                'menugroup': 'Credits'
            }
        )

        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Debits: recurring',
                'content': self._meta['recurring_debits'],
                'id': 'recurring_debits',
                'menugroup': 'Debits'
            }
        )

        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Debits: multiple',
                'content': self._meta['report_debit_regular'],
                'id': 'report_debit_regular',
                'menugroup': 'Debits'
            }
        )

        nice_new_report.add_main_box(
            {
                'icon': 'area-chart',
                'title': 'Debit report: one-offs',
                'content': self._meta['report_debit_oneoff'],
                'id': 'report_debit_oneoff',
                'menugroup': 'Debits'
            }
        )

        nice_new_report.add_side_nav_group(
            {
                'name': 'Debits',
                'icon': 'level-down',
                'items': [
                    {
                        'link': '#recurring_debits',
                        'label': 'Recurring',
                        'icon': 'recycle'
                    },
                    {
                        'link': '#report_debit_oneoff',
                        'label': 'One-offs',
                        'icon': 'window-maximize'
                    },
                    {
                        'link': '#report_debit_regular',
                        'label': 'Multiple',
                        'icon': 'window-restore'
                    }
                ]
            }
        )

        nice_new_report.add_side_nav_group(
            {
                'name': 'Credits',
                'icon': 'level-up',
                'items': [
                    {
                        'link': '#recurring_credits',
                        'label': 'Recurring',
                        'icon': 'recycle'
                    },
                    {
                        'link': '#report_credit_oneoff',
                        'label': 'One-offs',
                        'icon': 'window-maximize'
                    },
                    {
                        'link': '#report_credit_regular',
                        'label': 'Multiple',
                        'icon': 'window-restore'
                    }
                ]
            }
        )

        nice_new_report.add_value_card(
            {
                'state': 'danger',
                'icon': 'gbp',
                'body': '{:20,.2f}'.format(float(self._meta['balance']['open'])),
                'linklabel': 'Opening balance'
            }
        )
        nice_new_report.add_value_card(
            {
                'state': 'success',
                'icon': 'gbp',
                'body': '{:20,.2f}'.format(float(self._meta['balance']['close'])),
                'linklabel': 'Closing balance'
            }
        )

        nice_new_report.add_value_card(
            {
                'state': 'info',
                'icon': 'gbp',
                'body': '{:20,.2f}'.format(float(self._meta['total_credit'])),
                'linklabel': 'Total credit'
            }
        )

        nice_new_report.add_value_card(
            {
                'state': 'warning',
                'icon': 'gbp',
                'body': '{:20,.2f}'.format(float(self._meta['total_debit'])),
                'linklabel': 'Total debit'
            }
        )

        desc = self._meta['meta']['description'].split('-')
        nice_new_report.set_top_matter(
            [desc[0],
             desc[1] + ' (' + self._meta['period']['begin'] + ')',
             desc[2] + ' (' + self._meta['period']['end'] + ')']
        )

        nice_new_report.add_pie(pie=self._meta['top5_oneoff_debit_pie'],
                                title='Top 5 one off debits')

        return nice_new_report.get()
