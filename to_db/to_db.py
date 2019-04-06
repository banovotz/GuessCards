from config import config
from shuffle import shuffle
from draw import draw
from dimensions.sum_of_all_numbers import sum_of_all_numbers
import pickledb

class ToDb:
    SH=shuffle.Shuffle()
    DC= draw.DrawCards()
    SAN = sum_of_all_numbers.SumOfAllNumbers()

    def to_db(self):
        cards_and_dimensions_db = pickledb.load(config.CARDS_AND_DIMENSIONS_PICKLE_DB, False)

        i=0
        while i < 3:


            drawn_cards = self.DC.drawCards(self.SH.shuffleCards(), config.CARDS_TO_DRAW)
            sum_of_drawn_cards_with_numbers = self.SAN.sumOfAllNumbers(drawn_cards)
            drawn_cards.update({"sum_of_drawn_cards_with_numbers": sum_of_drawn_cards_with_numbers})
            cards_and_dimensions_db.set(str(i), drawn_cards)

            i=i+1

        cards_and_dimensions_db.dump()
        return cards_and_dimensions_db


