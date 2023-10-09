T = int(input())
for test_case in range(1, T+1):
    N= int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    num_list = list(map(str, num_list))
    print(f'#{test_case}', ' '.join(num_list))