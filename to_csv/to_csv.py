from config import config
import csv
import pickledb
cards_and_dimensions_db = pickledb.load(config.CARDS_AND_DIMENSIONS_PICKLE_DB, False)

class ToCsv:
    def write_csv(self):

        with open(config.CARDS_AND_DIMENSIONS_CSV, mode='w') as csv_file:
            fieldnames = cards_and_dimensions_db.dkeys("0")
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in cards_and_dimensions_db.getall():
                writer.writerow(cards_and_dimensions_db.dgetall(i))



