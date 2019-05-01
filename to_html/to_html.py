from config import config
from helpers.html_3rd import html3rd
import csv
from word2number import w2n


class ToHtml:
    H = html3rd.HTML()

    def to_html(self):
        t=self.H.table(border='1', id="carddata")
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

        html_human_play_before="""
        <html>
        
        <head>
        </head>
        
        <body onload="init()">
        
        <style>
        #carddata {display: none;}
        #play_area {padding-top: 50;
                   padding-bottom: 30;
                   text-decoration: none;
                   text-transform: uppercase;}
        .dimension_name {color: transparent;
                         text-align: center;}
        .dimension_value {color: transparent;
                          text-align: center;}
        .rule_name {color: transparent;
                    text-align: center;}
        .rule_bool {text-transform: uppercase;
                    color: ffffff;
                    text-align: center;}
        body {background-color: 496D89;}
        #play, #reveal, #hide {background-color: #123652; 
                border: none;
                color: white;
                padding-top: 20;
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

        html_human_play_after="""
        <div id="play_area">
        
        <table id="play_table"></table>
        <p id="rule_display">&nbsp;<p>       
        </div>
        
        
        <button type="Button" id="play" name="Play" onclick="toggleTable()">Draw</button>
        <button type="Button" id="reveal" name="Reveal" onclick="revealRule()">Reveal rule</button>
        <button type="Button" id="hide" name="Hide" onclick="hideRule()">Restart</button>   
 
        
        <script>
        function toggleTable() {
            var i;
            var rows_count= document.getElementById("carddata").rows.length;
            i = Math.floor(Math.random() * rows_count-2) + 2;
            j=i.toString();
            document.getElementById('play_table').innerHTML = document.getElementById(j).innerHTML; 
        }
        </script>
        
        <script>
        function revealRule() {
            var item_count = document.getElementsByClassName('rule_name').length;
            document.getElementsByClassName('rule_bool')[item_count-1].style.color= "transparent";   
            document.getElementById('rule_display').innerHTML =  "True if " +
            document.getElementsByClassName('dimension_name')[item_count-1].innerHTML + "&nbsp;("  +
            document.getElementsByClassName('dimension_value')[item_count-1].innerHTML + ")&nbsp;" +
            document.getElementsByClassName('rule_name')[item_count-1].innerHTML + "." + "&nbsp;" + "This hand is " +
            document.getElementsByClassName('rule_bool')[item_count-1].innerHTML;
            document.getElementById('rule_display').style.color="ffffff";
            document.getElementsByClassName('rule_bool').style.color="green";
            
        }  
        </script>         
        <script>
        function hideRule() {
        document.getElementById('rule_display').style.color="transparent";
        toggleTable();
    
        }
        </script>
        
       
        </body>
        </html>
        
        """

        html_ai_play_before = """
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script>
        <script type="text/javascript">
        var auto_refresh = setInterval(function () {
                                        $('#play_area').load('#play_area');
                                        }, 1000);

        </script>
        """
        print(str(html_human_play_before) + str(t) + str(html_human_play_after))

        return str(html_human_play_before) + str(t) + str(html_human_play_after)



