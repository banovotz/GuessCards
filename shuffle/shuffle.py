import requests
import json

class Shuffle:
    deck_of_cards_api="https://deckofcardsapi.com/api/"
    url = deck_of_cards_api + "deck/new/shuffle/?deck_count=1"
    headers = {
        'Cache-Control': "no-cache",

    }
    first_response = requests.request("GET", url, headers=headers)

    first_deck = json.loads(first_response.text)

    DECK_ID = first_deck["deck_id"]

    def shuffleCards(self):
        url = self.deck_of_cards_api + "/deck/"+ self.DECK_ID + "/shuffle/"

        headers = self.headers

        response = requests.request("GET", url, headers=headers)

        deck = json.loads(response.text)
        deck_id=deck["deck_id"]
        return deck_id



