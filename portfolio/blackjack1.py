class Card:
    def __init__(self):
        self.name = "카드"
        
    def card(self):
        import random
        s = ["Spade", "Diamond", "Heart", "Clover"]
        n = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = []
        i = random.choice(s)
        j = random.choice(n)
        a = [i + j]
        print(a)

카드 = Card()
카드.card()
