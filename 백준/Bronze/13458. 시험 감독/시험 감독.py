import sys
import math
input = sys.stdin.readline
# 입력값 받기
n_room = int(input())
studentcount_list = list(map(int, input().split()))
n_boss, n_semi = list(map(int, input().split()))
calculator_list = []

# 나누기를 통해서 알아 낸다
for item in studentcount_list:
    if item <= n_boss:
        calculator_list.append(1)
    else:
        calculator_list.append(math.ceil(1 + (item-n_boss)/n_semi))
print(sum(calculator_list))
