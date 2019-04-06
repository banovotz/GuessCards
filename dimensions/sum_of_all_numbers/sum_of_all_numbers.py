from config import config
import re
import pickledb

class SumOfAllNumbers:
    def sumOfAllNumbers(self, cards):
        cards_list=[]
        cards_numbers = []
        for key,value in cards.iteritems():
            cards_list.append(value)
        for card in cards_list:
            if re.findall('\d+', str(card)):
                cards_numbers.append(int(re.findall('\d+', str(card))[0]))

        card_numbers_normalized_tens=[]
        for card_number in cards_numbers:
            if card_number == 0:
                card_number = 10
            else:
                card_number = card_number
            card_numbers_normalized_tens.append(card_number)
        sum_of_all_cards=str(sum(card_numbers_normalized_tens))

        return sum_of_all_cards


