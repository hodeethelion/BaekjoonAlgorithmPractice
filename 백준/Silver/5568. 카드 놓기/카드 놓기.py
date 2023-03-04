#카드 놓기
number_cards = int(input())
select_number = int(input())
cards_list = []
for i in range(number_cards):
    cards_list.append(input())
from itertools import permutations
new_list = list(permutations(cards_list, select_number))
# print(new_list)
combo = []
for item in new_list:
    temp = ''
    for k in item:
        temp = temp + k
    combo.append(temp)
combo = list(set(combo))
# print(combo)
print(len(combo))