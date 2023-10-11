T = int(input())
for test_case in range(1, T+1):
    sample_list = list(map(int, input().split()))
    if sample_list[0] + sample_list[2] == 2* sample_list[1]:
        answer = 0

    else:
        # 첫번째가 바꿔야하는 것이라면
        ans_list = [2*sample_list[1] - sample_list[2] - sample_list[0],
                    2*sample_list[1] - sample_list[0] - sample_list[2],
                    0.5*(sample_list[0] + sample_list[2]) - sample_list[1]]
        ans_list = list(map(abs, ans_list))
        answer = min(ans_list)
    print(f'#{test_case} {answer:.1f}')