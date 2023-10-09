def compare_list(sample_list):
    sample_list.sort()
    if sample_list == list(range(1, 10)):
        return 1
    else:
        return 0


T = int(input())

for test_case in range(1, T+1):
    sudoku = []
    check_case = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    check_case += sudoku
    # 세로
    for i in range(9):
        add_list = []
        for j in range(9):
            add_list.append(sudoku[j][i])
        check_case.append(add_list)
    # 네모 모양
    for set_index in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
        row, col = set_index
        add_list = []
        for i in range(3):
            for j in range(3):
                add_list.append(sudoku[row + i][col + j])
        check_case.append(add_list)
    answer = 1
    for candidate in check_case:
        if compare_list(candidate) == 0:
            answer = 0
            break
    print(f'#{test_case} {answer}')