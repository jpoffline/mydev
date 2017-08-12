import csv

class DUMPABLE(object):
    def __init__(self):
        pass

    def data(self):
        """
        Data; needs to
        be overridden by inheriting
        class
        """
        pass
    
    def header(self):
        """
        Header data; needs to
        be overridden by inheriting
        class
        """
        pass


    def to_csv(self,filename):
        print '* writing to file', filename
        with open(filename, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(self.header())
            for line in self.data():
                writer.writerow(line)

    def to_html_table(self, filename=None):
        html = "<table>"

        hd = ""
        row = ""
        for r in self.header():
            row += "<td><b>" + str(r) + "</b></td>"
        hd += "<tr>" + row + "</tr>"
        data = self.data()
        for r in data:
            row = ""
            for i in r:
                row += "<td>" + str(i) + "</td>"
            hd += "<tr>" + row + "</tr>"
        html += hd + "</table>"
        if filename is None:
            return html
        display = open(filename, 'w')
        display.write(html)
        display.close()