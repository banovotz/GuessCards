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
TC=to_csv.ToCsv()
P=predict.Predict()
IP=is_prime.IsPrime()
TH=to_html.ToHtml()
def switch_dimensions(drawn_cards):
    dimensions_switch = {"sum_of_all_cards_with_numbers": SAN.sumOfAllNumbers(drawn_cards)}
    return dimensions_switch


class Run:


    def generate_list(self, dimension, list_len, rule):


        i=0

        while i < list_len:

            drawn_cards = DC.drawCards(SH.shuffleCards(), config.CARDS_TO_DRAW)
            dimension_name = switch_dimensions(drawn_cards)[dimension][1]
            dimension_value = switch_dimensions(drawn_cards)[dimension][0]

            if rule[0] == "gt":
                rule_name="greater than " + rule[1]
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
        TC.write_csv()

R=Run()
#R.generate_list("sum_of_all_cards_with_numbers", 100, ["gt", 15])
R.generate_list("sum_of_all_cards_with_numbers", 100, ["prime", True])

RC=RunCsv()
RC.generate_csv()

P.predict_bool()

TH.to_html()