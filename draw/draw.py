from shuffle import shuffle
from config import config
import requests
import json


class DrawCards:
    def drawCards(self, deck_id, cards_to_draw):

        drawn = []

        url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + str(cards_to_draw)

        headers = {
        'Cache-Control': "no-cache",

        }

        response = requests.request("GET", url, headers=headers)


        drawn_json = json.loads(response.text)

        i=0
        while i < cards_to_draw:
            drawn.append(drawn_json["cards"][i]["code"])
            i=i+1
        print drawn
        return drawn

DC= DrawCards()
DC.drawCards(shuffle.DECK_ID, config.CARDS_TO_DRAW)