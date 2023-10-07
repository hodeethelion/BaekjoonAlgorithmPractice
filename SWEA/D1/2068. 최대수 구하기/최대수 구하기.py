T = int(input())
for test_case in range(1, T + 1):
    number_list = list(map(int, input().split()))
    answer = 0
    for item in number_list:
        if answer < item:
            answer = item
    print(f'#{test_case} {answer}')