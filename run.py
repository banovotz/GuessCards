from gooey import Gooey, GooeyParser
import webview
import threading
from config import config
from shuffle import shuffle
from draw import draw
from to_db import to_db
from to_csv import to_csv
from to_html import to_html
from predict import predict
from dimensions.sum_of_all_numbers import sum_of_all_numbers
from helpers.is_prime import is_prime

SH = shuffle.Shuffle()
DC = draw.DrawCards()
SAN = sum_of_all_numbers.SumOfAllNumbers()
TD=to_db.ToDb()
P=predict.Predict()
IP=is_prime.IsPrime()
TH=to_html.ToHtml()

def switch_dimensions(drawn_cards):
    dimensions_switch = {"sum_of_all_cards_with_numbers": SAN.sumOfAllNumbers(drawn_cards)}
    return dimensions_switch


class Run:


    def generate_list(self, dimension, list_len, rule):


        i=0


        while i < int(list_len):

            drawn_cards = DC.drawCards(SH.shuffleCards(), config.CARDS_TO_DRAW)
            dimension_name = switch_dimensions(drawn_cards)[dimension][1]
            dimension_value = switch_dimensions(drawn_cards)[dimension][0]

            if rule[0] == "gt":
                rule_name="greater than " + str(rule[1])
                if int(dimension_value) > int(rule[1]):
                    rule_bool="true"
                else:
                    rule_bool="false"

            elif rule[0] == "prime":
                print ("usli u prime")
                if rule[1] == True:
                    rule_name="is prime"

                    if IP.is_prime(int(dimension_value)) == True:
                        print("prime je " + dimension_value)
                        rule_bool="true"
                    else:
                        print("nije prime " + dimension_value)
                        rule_bool = "false"
            else:
                rule_bool = "rule_not_suppported"

            TD.to_db(dimension_name, dimension_value, drawn_cards, rule_bool, rule_name, i)
            i=i+1




class RunCsv:
    def generate_csv(self):
        TC = to_csv.ToCsv()
        TC.write_csv()
program_description='Generate hands of cards'
@Gooey(
       navigation='TABBED',
       default_size=(800, 600),
       image_dir='res',
       program_name='Guess The Game',
       program_description=program_description,
       show_success_modal=False,
       header_show_subtitle=False)
def main():

    parser = GooeyParser()

    subparser = parser.add_subparsers()
    dimensions_parser=subparser.add_parser('dimensions')

    dimensions_parser.add_argument('--dimension', dest='dimension_value', help='dimension to run', required=True)
    dimensions_parser.add_argument('--list_len', dest='list_len_value', help='list length', required=True)
    dimensions_parser.add_argument('--rule_name', dest='rule_name_value', help='rule name', required=True)
    dimensions_parser.add_argument('--param', dest='rule_param_value', help='rule param', required=True)


    preview_parser = subparser.add_parser('play')
    preview_parser.add_argument('--do_preview', widget='Dropdown', dest='do_preview_value', choices=["play as human", "let ML guess"])


    results=parser.parse_args()

    try:
        if results.do_preview_value  == "play as human":
            def display_html():
                html_to_display=TH.to_html()
                webview.load_html(html_to_display)


            t = threading.Thread(target=display_html)
            t.start()
            webview.create_window('Play', width=850, height=600)


    except:
        R = Run()
        print("Generating list of " + str(results.list_len_value) + " hands with " + str(config.CARDS_TO_DRAW) + " cards")
        R.generate_list(results.dimension_value, results.list_len_value, [results.rule_name_value, results.rule_param_value])
        RC = RunCsv()
        RC.generate_csv()



#P.predict_bool()

main()