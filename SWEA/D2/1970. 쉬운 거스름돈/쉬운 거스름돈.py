money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for test_case in range(1, T+1):
    total_money = int(input())
    ans_list = []
    for cash in money_list:
        count = total_money // cash
        total_money -= (count * cash)
        ans_list.append(str(count))
    print(f'#{test_case}')
    print(' '.join(ans_list))