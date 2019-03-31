import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

headers = {
    'Cache-Control': "no-cache",

    }

response = requests.request("GET", url, headers=headers)

deck = json.loads(response.text)


DECK_ID = deck["deck_id"]

