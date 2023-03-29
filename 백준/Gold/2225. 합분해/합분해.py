import sys
input = sys.stdin.readline
total_sum, k = map(int, input().split())

if k == 1:
    print(1)
elif k == 2:
    print((total_sum+1)%1000000000)
elif k>=3:
    dp= [[0] * (total_sum+1) for _ in range(k+1)]

    for index, item in enumerate(dp[1]):
        if index == 0:
            continue
        else: 
            dp[1][index] = 1

    # for i in dp:
    #     print(i)

    for i in range(2, k+1):
        for j in range(1, total_sum+1):
            dp[i][j] = sum(dp[i-1][:j+1]) + 1
    print(dp[-1][-1]%1000000000)