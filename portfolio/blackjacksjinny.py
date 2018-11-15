class Card:
    def __init__(self, s, n):
        self.s = s
        self.n = n

    def card(self):
        import random
        s = ["Spade", "Diamond", "Heart", "Clover"]
        n = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card = []
        i = random.choice(s)
        j = random.choice(n)
        a = i + j
        card.append(a)
        print(card)
        return card
        
    def sum(self, x, y):
        b = x + y
        return sum(b)


카드 = Card(s,n)
카드.card()


# class Person:
#     def __init__(self):
#         self.name = "사용자"
#     def sum(self, x, y):
#         return x + y

#     class Dealer(Person):
#         name = "딜러"
        
#     class Player(Person):
#         name = "플레이어"


    # class Deck(Card):
    #     def __init__(self, s, n):
    #         self.s = "모양"
    #         self.n = "숫자"

#     hos = input("Hit or stay? >>>")

#     def deck(self):
#         if card == hit:
#             card.join(list(card))


# class Person:
#     def __init__(self):
#         self.name = "사용자"
#     def sum(self, x, y):
#         return sum += x + y


# class Dealer(Person):
#     name = "딜러"

# class Player(Person):
#     name = "플레이어"

# 딜러 = Dealer
# 플레이어 = Player


#######################################

# from functools import reduce
# product = 1
# lst = [1, 2, 3, 4]
# for num in lst:
#     product = product * num

# print("product1>>", product)

# product2 = reduce(lambda x, y: x * y, lst)
# print("product2>>", product2)


######################################3
