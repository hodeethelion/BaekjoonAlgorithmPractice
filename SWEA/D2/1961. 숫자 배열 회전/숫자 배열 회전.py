def rotate(table_map):
    n = len(table_map[0])
    rotated_list = []
    for _ in range(n):
        rotated_list.append([0 for _ in range(n)])
    for i in range(n):
        for j in range(n):
            rotated_list[i][j] = table_map[n-1-j][i]
    return rotated_list

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))
    rotate_90 = rotate(table)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    print(f'#{test_case}')
    total_answer = []
    for idx in range(N):
        answer = []
        answer.append(''.join(list(map(str, rotate_90[idx]))))
        answer.append(''.join(list(map(str, rotate_180[idx]))))
        answer.append(''.join(list(map(str, rotate_270[idx]))))
        total_answer.append(answer)
    for setting in total_answer:
        print(' '.join(setting))
  