import csv
from plotly import tools as plytools
import plotly
import plotly.graph_objs as go

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


    def content(self):
        pass

    def to_file(self, filename):
        display = open(filename, 'w')
        display.write(self.content())
        display.close()

    def to_csv(self, filename):
        print '* writing to file', filename
        with open(filename, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(self.header())
            for line in self.data():
                writer.writerow(line)

    def bs_table(self):
        return "<table class='table table-striped table-condensed table-hover' style='font-size:60%;'>"

    def to_html_table(self, filename=None, topn=None):

        html = self.bs_table()
        hd = ""
        row = ""
        for r in self.header():
            row += "<td><b>" + str(r) + "</b></td>"
        hd += "<tr>" + row + "</tr>"
        data = self.data()
        if topn is not None:
            data = data[:topn]
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


    def to_plot_pie(self, idxs,topn=5):
        data = self.data()
        if topn is not None:
            data = data[:topn]
        
        idx_data = idxs['values']
        idx_labels = idxs['labels']
        values = [
            v[idx_data] for v in data
        ]
        labels = [
            v[idx_labels] + '<br>' + str(v[idxs['labels2'][0]]) + idxs['labels2'][1] for v in data
        ]
        
        trace = go.Pie(labels=labels, values=values)
        return plotly.offline.plot([trace],
                               show_link=False,
                               output_type="div",
                               include_plotlyjs=False)