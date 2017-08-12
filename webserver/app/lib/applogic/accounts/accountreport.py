
class accountreport(object):
    def __init__(self, filename, meta):
        self._filename = filename
        self._meta = meta

    def create(self):
        report = "<h1>Account report</h1>"
        report += "<h2>Period: " + \
            self._meta['period']['begin'] + " to " + \
            self._meta['period']['end'] + "</h1>"
        report += "<h2>Total debit: " + self._meta['total_debit'] + "</h2>"
        report += "<h2>Total credit: " + self._meta['total_credit'] + "</h2>"
        report += "<table>"
        report += "<tr><td><h1>Debit report: regular</h1></td>"
        report += "<td><h1>Credit report: regular</h1></td></tr>"
        report += "<tr><td>" + self._meta['report_debit_regular'] + "</td>"
        report += "<td>" + self._meta['report_credit_regular'] + "</td></tr>"
        report += "<tr><td><h1>Debit report: one-offs</h1></td>"
        report += "<td><h1>Credit report: one-offs</h1></td></tr>"
        report += "<tr><td>" + self._meta['report_debit_oneoff'] + "</td>"
        report += "<td>" + self._meta['report_credit_oneoff'] + "</td></tr>"
        report += "</table>"

        display = open(self._filename, 'w')
        display.write(report)
        display.close()
