class Card:
    def card(self):
        
        shape = ["S", "D", "H", "C"]
        number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        point = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
        points = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4

        card = {}
        for i in range(13):
            card[number[i]] = point[i] 

        print(card)

        y = list(card.keys())
        print(y)

        score = []
        for i, j in enumerate(shape):
            for v, w in enumerate(number):
                a = j + w
                score.append(a)

        print(score)

        cards = {}
        for i in range(52):
            cards[score[i]] = points[i]                  

        print(cards)

        return cards


cards = card()