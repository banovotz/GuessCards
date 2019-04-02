from config import config
import re
import pickledb
dimensions_db=pickledb.load('dimenzije.db', False)
class SumOfAllNumbers:
    def sumOfAllNumbers(self, cards):
        cards_list=[]
        cards_numbers = []
        for key,value in cards.iteritems():
            cards_list.append(value)
        #print cards_list
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


        #print(cards_numbers)
        #print(card_numbers_normalized_tens)
        #print(sum(cards_numbers))
        sum_of_all_cards=sum(card_numbers_normalized_tens)

       #print(sum_of_all_cards)
        dimensions_db.set('sum_of_all_cards', sum_of_all_cards)
        dimensions_db.dcreate("perica")
        dimensions_db.dadd("perica", ("sum_of_all_cards", sum_of_all_cards))
        dimensions_db.dgetall('sum_of_all_cards')
        dimensions_db.dump()
        return sum_of_all_cards


