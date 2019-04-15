from config import config
from html import HTML
import csv

H=HTML()
class ToHtml:
    def to_html(self):
        t=H.table(border='2')
        r = t.tr
        with open(config.CARDS_AND_DIMENSIONS_CSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for column in reader.fieldnames:
                r.td(column)
            for row in reader:
                t.tr
                for col in row.iteritems():
                    t.td(col[1])
        print t


