import sys
from collections import deque
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    n_coin = int(input())
    coin_list = list(map(int, input().split()))
    target = int(input())
    count_coin = [0 for _ in range(target+1)]
    count_coin[0] = 1 

    for coin in coin_list:
        for i in range(1, target+1):
            if i>=coin:
                count_coin[i] += count_coin[i-coin]
    print(count_coin[target])