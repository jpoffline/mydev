
import csv

def dump(filename, header, data):
    print 'Writing to file', filename
    with open(filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(header)
        for line in data:
            writer.writerow(line)