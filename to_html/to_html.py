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
                             id=col[0]+str(reader.line_num),
                             klass=col[0])
                    except:
                        t.td(col[1], klass=col[0], id=col[0]+str(reader.line_num))

        html_app_before="""
        <html>
        <head>
        </head>
        <body onload="init()">
        <style>
        #carddata {display: none;}
        .dimension_name {color: transparent;}
        .dimension_value {color: transparent;}
        .rule_name {color: transparent;}
        .rule_bool {text-transform: uppercase;
                    color: ffffff;}
        body {background-color: 496D89;}
        #play, #reveal {background-color: #123652; 
                border: none;
                color: white;
                padding: 45px 85px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;}
        

        </style>
    
        
        <script>
        function init() {
        pywebview.api.init()
        </script>       
        

        """

        html_app_after="""
        <table id="button_play"> 
        <button type="Button" id="play" name="Play" onclick="toggleTable()">Draw</button>
        <button type="Button" id="reveal" name="Reveal" onclick="revealRule()">Reveal rule</button>
        
        </table>
    

        <script>
        function toggleTable() {
            var i;
            var rows_count= document.getElementById("carddata").rows.length;
            i = Math.floor(Math.random() * rows_count-2) + 2;
            j=i.toString();
            document.getElementById('button_play').innerHTML = document.getElementById(j).innerHTML; 
        }
        
        </script>
        <script>
        function revealRule() {
            var item_count = document.getElementsByClassName('rule_name').length;

            document.getElementsByClassName('dimension_name')[item_count-1].style.color = "ffffff";
             document.getElementsByClassName('dimension_value')[item_count-1].style.color = "ffffff";
            document.getElementsByClassName('rule_name')[item_count-1].style.color = "ffffff";
            
            
        }
        
        </script>
               
        
        </body>
        </html>
        
        """

        print(str(html_app_before) + str(t) + str(html_app_after))

        return str(html_app_before) + str(t) + str(html_app_after)



