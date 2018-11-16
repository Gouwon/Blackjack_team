def score(dh, ph):
	if total(ph) == 21:
		print(dh, ph)
		print ("You've got a Blackjack!\n")
	elif total(dh) == 21:
		print(dh, ph)		
		print("The dealer've got a blackjack.\n")
	elif total(ph) > 21:
		print(dh, ph)
		print ("Sorry. You've lost.\n")
	elif total(dh) > 21:
		print(dh, ph)			   
		print ("You've won.\n")
	elif total(ph) < total(dh):
		print(dh, ph)
        print("You've lost.\n")
	elif total(ph) > total(dh):
		print(dh, ph)			   
		print("You've won.\n")

