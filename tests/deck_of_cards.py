import requests

deck_count = "1"
URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + deck_count
r = requests.get(url=URL)
data = r.json()
deck_id = data['deck_id']


amount_to_draw = "2"
draw_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + amount_to_draw
r = requests.get(url=draw_url)
data = r.json()

#print(data)

#cards = data['cards'][0] # first card
card = data['cards'][0]

value = card['value']
suit = card['suit']

print(f'{value} of {suit}')