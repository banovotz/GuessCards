import requests
import json

class Shuffle:
    def shuffleCards(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

        headers = {
            'Cache-Control': "no-cache",

            }

        response = requests.request("GET", url, headers=headers)

        deck = json.loads(response.text)


        DECK_ID =  deck["deck_id"]
        return DECK_ID

#"5xdqigk03g9f"
