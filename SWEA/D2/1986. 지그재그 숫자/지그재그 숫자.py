T = int(input())
for test_case in range(1, T+1):
    end_number = int(input())
    ans = 0
    for i in range(1, end_number+1):
        if i % 2 == 0:
            ans -= i
        else:
            ans += i
    print(f'#{test_case} {ans}')
