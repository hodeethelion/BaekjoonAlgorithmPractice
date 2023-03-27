import sys
input = sys.stdin.readline
n_type, n_sum = map(int, input().split())
coin_list =[]
for _ in range(n_type):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
# print(coin_list)
count = 0
for item in coin_list:
    tmp = n_sum // item
    count += tmp
    n_sum -= item*tmp
    # print('item', count)

print(count)