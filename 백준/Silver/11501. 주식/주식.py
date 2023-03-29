import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    n_days = int(input())
    stock_days = list(map(int, input().split()))
    stock_days.reverse()

    max_p = 0
    profit = 0
    # print(stock_days)
    for item in stock_days:
        if item > max_p:
            max_p = item
        else:
            profit += (max_p - item)
            # print(max_p - item)
    print(profit)