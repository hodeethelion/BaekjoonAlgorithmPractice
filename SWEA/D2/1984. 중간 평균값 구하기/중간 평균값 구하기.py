T = int(input())
for test_case in range(1, T+1):
    all_number = list(map(int, input().split()))
    mean = (sum(all_number) - max(all_number) - min(all_number)) / (len(all_number)-2)
    print(f'#{test_case} {round(mean)}')