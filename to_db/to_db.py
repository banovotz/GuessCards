from config import config
import pickledb

class ToDb:


    def to_db(self, dimension_name, dimension_value, drawn_cards, rule_bool, rule_name, i):

        cards_and_dimensions_db = pickledb.load(config.CARDS_AND_DIMENSIONS_PICKLE_DB, False)


        drawn_cards.update({dimension_name: dimension_value})
        drawn_cards.update({"rule_name": rule_name})
        drawn_cards.update({"rule_bool": rule_bool})
        cards_and_dimensions_db.set(str(i), drawn_cards)


        cards_and_dimensions_db.dump()
        return cards_and_dimensions_db


