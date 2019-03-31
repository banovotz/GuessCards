from config import config
from shuffle import shuffle
from draw import draw
from dimensions.sum_of_all_numbers import sum_of_all_numbers

DC= draw.DrawCards()
SAN = sum_of_all_numbers.SumOfAllNumbers()
cards_to_sum=DC.drawCards(shuffle.DECK_ID, config.CARDS_TO_DRAW)

print(SAN.sumOfAllNumbers(cards_to_sum))



