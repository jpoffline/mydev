
from dumpable import DUMPABLE
import app.lib.widgets.bswidgets as bswidgets
import html_report as html_report
import datetime as datetime


class accountreport(DUMPABLE):
    def __init__(self, filename, meta):
        self._filename = filename
        self._meta = meta
        self._report = ''

    def get_report_css(self):
        return """
        <link rel="stylesheet" href= "static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/dashboard.css">
    <script src="static/js/plotly-180717.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
    <script src="static/js/jquery-180717.js"></script>
    <script src="static/js/d3-180717.js"></script>
    <link rel="stylesheet" href="static/css/font-awesome.min.css">
    <!--<link href="static/css/sb-admin.css" rel="stylesheet">-->
    """

    def content(self):
        return self._report

    def create(self):

        box_open = {
            'boxtype': 'danger',
            'icon': 'gbp',
            'boxtext': 'Opening balance',
            'boxvalue': self._meta['balance']['open']
        }

        box_close = {
            'boxtype': 'success',
            'icon': 'gbp',
            'boxtext': 'Closing balance',
            'boxvalue': self._meta['balance']['close']
        }

        box_total_credit = {
            'boxtype': 'success',
            'icon': 'gbp',
            'boxtext': 'Total credit',
            'boxvalue': self._meta['total_credit']
        }

        box_total_debit = {
            'boxtype': 'success',
            'icon': 'gbp',
            'boxtext': 'Total debit',
            'boxvalue': self._meta['total_debit']
        }

        box_counts = {
            'boxtype': 'info',
            'icon': 'record',
            'boxtext': 'Num items',
            'boxvalue': self._meta['count_items']['total']
        }

        boxes = bswidgets.bsValueBox(
            [box_counts, box_total_credit, box_total_debit, box_open, box_close])
        report = "<h1>Account report</h1>"
        report += "<h2>Period: " + \
            self._meta['period']['begin'] + " to " + \
            self._meta['period']['end'] + "</h1>"
        report += boxes.get()
        report += bswidgets.inWell_title("Debits: recurring",
                                         self._meta['recurring_debits'], 'recurring_debits').get()
        report += bswidgets.inWell_title("Credits: recurring",
                                         self._meta['recurring_credits'], 'recurring_credits').get()
        report += bswidgets.inWell_title("Debit report: multiple",
                                         self._meta['report_debit_regular'], 'report_debit_regular').get()

        report += bswidgets.inWell_title("Debit report: one-offs",
                                         self._meta['report_debit_oneoff'], 'report_debit_oneoff').get()
        report += bswidgets.inWell_title("Credit report: multiple",
                                         self._meta['report_credit_regular'], 'report_credit_regular').get()
        report += bswidgets.inWell_title("Credit report: one-offs",
                                         self._meta['report_credit_oneoff'], 'report_credit_oneoff').get()

        meta = {
            'head': self.get_report_css(),
            'content': report
        }

        self._report = self._template(meta)

        self.to_file(self._filename)
        nice_new_report = html_report.htmlreport({
            'update': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

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
                        'link': 'recurring_debits',
                        'label': 'Recurring',
                        'icon': 'recycle'
                    },
                    {
                        'link': 'report_debit_oneoff',
                        'label': 'One-offs',
                        'icon': 'window-maximize'
                    },
                    {
                        'link': 'report_debit_regular',
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
                        'link': 'recurring_credits',
                        'label': 'Recurring',
                        'icon': 'recycle'
                    },
                    {
                        'link': 'report_credit_oneoff',
                        'label': 'One-offs',
                        'icon': 'window-maximize'
                    },
                    {
                        'link': 'report_credit_regular',
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
            'body': str(self._meta['balance']['open']),
            'linklabel': 'Opening balance'
            }
        )
        nice_new_report.add_value_card(
            {
            'state': 'success',
            'icon': 'gbp',
            'body': str(self._meta['balance']['close']),
            'linklabel': 'Closing balance'
            }
        )


        nice_new_report.add_value_card(
            {
            'state': 'info',
            'icon': 'gbp',
            'body': str(self._meta['total_credit']),
            'linklabel': 'Total credit'
            }
        )

        nice_new_report.add_value_card(
            {
            'state': 'warning',
            'icon': 'gbp',
            'body': str(self._meta['total_debit']),
            'linklabel': 'Total debit'
            }
        )


        nice_new_report.set_top_matter(
            ["Period",
            self._meta['period']['begin'],
            self._meta['period']['end']]
        )

        nice_new_report.add_pie(pie=self._meta['top5_oneoff_debit_pie'],
        title='Top 5 one off debits')

        cont2 = nice_new_report.get()
        display = open(self._filename + '2.html', 'w')
        display.write(cont2)
        display.close()

    def _nav_side(self):
        return """
        <div class="col-sm-3 col-md-2 sidebar">
    <ul class="nav nav-sidebar">
                <li><a href='report.html'>Home</a></li>
                <li><a href='#report_debit_regular'>debit/multi</a></li>
                <li><a href='#report_debit_oneoff'>debit/one</a></li> 
                <li><a href='#recurring_debits'>debits/recurring</a></li> 
                <li><a href='#recurring_credits'>credits/recurring</a></li> 
                <li><a href='#report_credit_regular'>credit/multi</a></li>
                <li><a href='#report_credit_oneoff'>credit/one</a></li>
    </ul></div>
    """

    def _nav_top(self):
        return ''
        return """<nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="report.html" id="menu-toggle">Accounts report</a>
            </div>
            <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
                <li><a href='#report_debit_regular'>debit/multi</a></li>
                <li><a href='#report_debit_oneoff'>debit/one</a></li> 
                <li><a href='#recurring_debits'>debits/recurring</a></li> 
                <li><a href='#recurring_credits'>credits/recurring</a></li> 
                <li><a href='#report_credit_regular'>credit/multi</a></li>
                <li><a href='#report_credit_oneoff'>credit/one</a></li>
            </ul>
            </div>
        </div>
            </nav>
            """

    def _template(self, meta):
        navside = meta.get('navside', self._nav_side())
        navtop = meta.get('navtop', self._nav_top())
        return """
            <!doctype html>
            <html>
            <head>
                """ + meta['head'] + """
                <title>Account report</title>
            </head>
            <body>
                """ + navtop + """
                <div class="container-fluid">
                <div class="row">
                    """ + navside + """
                    <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
                        """ + meta['content'] + """
                        <div>
                        &copy; Copyright 2017 by <a href="http://www.jpoffline.com/">jpoffline</a>.
                        </div>
                    </div>
                </div>
                </div>
            </body>
            </html>
            """
