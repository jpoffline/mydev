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