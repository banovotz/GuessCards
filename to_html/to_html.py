from config import config
from helpers.html_3rd import html3rd

H=html3rd.HTML()

import csv
from word2number import w2n


#H=HTML()

class ToHtml:

    def to_html(self):
        t=H.table(border='1', id="carddata")
        r = t.tr
        with open(config.CARDS_AND_DIMENSIONS_CSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for column in reader.fieldnames:
                r.td(column)
            for row in reader:
                t.tr(id=str(reader.line_num))
                for col in row.items():

                    try:
                        w2n.word_to_num(col[0])

                        t.td("<img width='100' src='https://deckofcardsapi.com/static/img/"
                             + col[1]
                             + ".png'></img>",
                             escape=False,
                             id=col[0])
                    except:
                        t.td(col[1], id=col[0])

        html_app_before="""
        <html>
        <head>
        </head>
        <body onload="init()">
        <style>
        #carddata {display: none;}
        #button_play {color: transparent;}
        </style>
    
        
        <script>
        function init() {
        pywebview.api.init()
        </script>       
        

        """

        html_app_after="""
        <div id="button_play"> 
        <button type="Button" id="play" name="Play" onclick="toggleTable()">Play</button>
        </div>
        <script>
        function toggleTable() {
            var i;
            var rows_count= document.getElementById("carddata").rows.length;
            i = Math.floor(Math.random() * rows_count) + 2;
            j=i.toString();
            document.getElementById('button_play').innerHTML = document.getElementById(j).innerHTML + " <button type=\\"Button\\" id=\\"play\\" name=\\"Play\\" onclick=\\"toggleTable()\\">Play</button>";

        }
        
        </script>
               
        
        </body>
        </html>
        
        """

        print(str(html_app_before) + str(t) + str(html_app_after))

        return str(html_app_before) + str(t) + str(html_app_after)



