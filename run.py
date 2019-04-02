from config import config
from shuffle import shuffle
from draw import draw
from dimensions.sum_of_all_numbers import sum_of_all_numbers
import pickledb

SH=shuffle.Shuffle()
DC= draw.DrawCards()
SAN = sum_of_all_numbers.SumOfAllNumbers()
dimensions2_db=pickledb.load('dimenzije2.db', False)

i=0
while i < 2:

    drawn_cards = DC.drawCards(SH.shuffleCards(), config.CARDS_TO_DRAW)
    sum_of_drawn_cards_with_numbers = SAN.sumOfAllNumbers(drawn_cards)
    dimensions2_db.dcreate(str(i))
    dimensions2_db.dadd(str(i), ("cards", drawn_cards))
    dimensions2_db.dadd(str(i), ("sum_of_drawn_cards_with_numbers", sum_of_drawn_cards_with_numbers))
    i=i+1
dimensions2_db.dump()




