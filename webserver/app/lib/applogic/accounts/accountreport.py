
from dumpable import DUMPABLE
import app.lib.widgets.bswidgets as bswidgets


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

        box_counts = {
            'boxtype': 'info',
            'icon': 'record',
            'boxtext': 'Num items',
            'boxvalue': self._meta['count_items']['total']
        }

        boxes = bswidgets.bsValueBox([box_counts, box_open, box_close])

        totals_bit = "<h2>Total debit: " + self._meta['total_debit'] + "</h2>" +\
            "<h2>Total credit: " + self._meta['total_credit'] + "</h2>"

        report = "<h1>Account report</h1>"
        report += "<h2>Period: " + \
            self._meta['period']['begin'] + " to " + \
            self._meta['period']['end'] + "</h1>"
        report += boxes.get()
        report += bswidgets.inWell(totals_bit).get()
        report += bswidgets.inWell_title("recurring_debits",
                                         self._meta['recurring_debits'],'recurring_debits').get()        
        report += bswidgets.inWell_title("recurring_credits",
                                         self._meta['recurring_credits'],'recurring_credits').get()
        report += bswidgets.inWell_title("Debit report: multiple",
                                         self._meta['report_debit_regular'],'report_debit_regular').get()

        report += bswidgets.inWell_title("Debit report: one-offs",
                                         self._meta['report_debit_oneoff'],'report_debit_oneoff').get()
        report += bswidgets.inWell_title("Credit report: multiple",
                                         self._meta['report_credit_regular'],'report_credit_regular').get()
        report += bswidgets.inWell_title("Credit report: one-offs",
                                         self._meta['report_credit_oneoff'],'report_credit_oneoff').get()

        meta = {
            'head': self.get_report_css(),
            'content': report
        }

        self._report = self._template(meta)

        self.to_file(self._filename)

    def _nav_side(self):
        return """
        <div class="col-sm-3 col-md-2 sidebar">
    <ul class="nav nav-sidebar">
                    <li><a href='#report_debit_regular'>debit/multi</a></li>
                <li><a href='#report_debit_oneoff'>debit/one</a></li> 
                <li><a href='#report_credit_regular'>credit/multi</a></li>
                <li><a href='#report_credit_oneoff'>credit/one</a></li>
    </ul></div>
    """

    def _nav_top(self):
        return ''
        return """<nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="/" id="menu-toggle">Accounts report</a>
            </div>
            <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
                <li><a href='#report_debit_regular'>debit/multi</a></li>
                <li><a href='#report_debit_oneoff'>debit/one</a></li> 
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
