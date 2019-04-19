from config import config
from helpers.html_3rd import html3rd

H=html3rd.HTML()

import csv
from word2number import w2n


#H=HTML()

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
                for col in row.items():

                    try:
                        w2n.word_to_num(col[0])

                        t.td("<img width='60' src='https://deckofcardsapi.com/static/img/" + col[1] + ".png'></img>", escape=False)
                    except:
                        t.td(col[1])
        print(t)


