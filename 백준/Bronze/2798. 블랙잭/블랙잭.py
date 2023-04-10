import sys
import itertools
input = sys.stdin.readline
n, m = map(int, input().split())
card_list = list(map(int, input().split()))
combo3 = list(itertools.combinations(card_list,3))
# print(combo3)
maximum= sys.maxsize
ans_list = []
for item in combo3:
    temp = sum(item)
    if temp <= m:
        ans_list.append(temp)
print(max(ans_list))