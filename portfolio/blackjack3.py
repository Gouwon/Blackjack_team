def total(h):
    total = 0
    for card in h:
	    if card == "J" or card == "Q" or card == "K":
	        total += 10

	    elif card == "A":
	        if total >= 11:
                    total += 1
	        else: 
                total += 11
	                total += card

    return total
