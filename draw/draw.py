import requests
import json
import inflect

class DrawCards:
    def drawCards(self, deck_id, cards_to_draw):

        drawn = {}
        word = inflect.engine()


        url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + str(cards_to_draw)

        headers = {
        'Cache-Control': "no-cache",

        }

        response = requests.request("GET", url, headers=headers)


        drawn_json = json.loads(response.text)

        i=0

        while i < cards_to_draw:
            drawn.update({word.number_to_words(i+1): drawn_json["cards"][i]["code"]})
            i=i+1
        #print drawn
        return drawn
