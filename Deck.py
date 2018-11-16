## class card에서 만든 카드를 받아서 셔플하는 부분.
## return 셔플된 카드 리스트.
## 카드는 리스트로 해서 일단 오는 것으로 가정.
import random
from Card import Card

false_data = {"S2" : 2, "S3" : 3, "S4" : 4, "S5" : 5, "S6" : 6}
x = list(false_data.keys())
random.shuffle(x)

# Card.card()

# print(x)
popx = x.pop()
# print(x.pop())
# print(x)
# print(x.pop())
# print(x)
# print(x.pop())
# print(x)
print(popx)
dic = []
print(dic.append(popx))
# a = dic.append(popx)

# list(a)
# print(a)
exit()
# x = card()
## 들어오는 card는 딕셔너리 형태.
## 딕셔너리는 셔플을 할 수 없다.
## 딕셔너리의 키들을 뽑아서, 셔플하고, 그 키들을 이용하여 값들에 접근하자.

# def card_shuffle(x):
#     y = list(x.keys())
#     random.shuffle(y)
#     return y

# def card_give():

# card_shuffle(false_data).pop()

# print(card_shuffle(false_data))
# print(card_shuffle(false_data).pop())
# print(card_shuffle(false_data))
# print(card_shuffle(false_data).pop())
# print(card_shuffle(false_data))
# print(card_shuffle(false_data).pop())

# print(false_data)
# print(type(false_data))
# print(false_data.keys())

# y = list(false_data.keys())
# print(card_shuffle(false_data))


l = [1,2,3,4,5]

print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())

