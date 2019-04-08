from config import config
from shuffle import shuffle
from draw import draw
from to_db import to_db
from dimensions.sum_of_all_numbers import sum_of_all_numbers

SH = shuffle.Shuffle()
DC = draw.DrawCards()
SAN = sum_of_all_numbers.SumOfAllNumbers()
TD=to_db.ToDb()


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
                if int(dimension_value) > int(rule[1]):
                    rule_bool="true"
                else:
                    rule_bool="false"
            else:
                rule_bool="rule_not_suppported"

            TD.to_db(dimension_name, dimension_value, drawn_cards, rule_bool, i)
            i=i+1

R=Run()
R.generate_list("sum_of_all_cards_with_numbers", 3, ["gt", 15])