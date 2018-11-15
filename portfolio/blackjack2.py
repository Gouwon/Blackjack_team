deck = ["2","3","4","5","6", "7", "8", "9","10","10","10","10","11"]*4

import random
def deal(deck):
    h = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop(i)
	    if card == deck[9]:card = "J"
	    if card == deck[10]:card = "Q"
	    if card == deck[11]:card = "K"
	    h.append(card)
    return h
print(deck)

deck.pop()