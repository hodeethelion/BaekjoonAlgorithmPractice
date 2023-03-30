import sys
input = sys.stdin.readline
n_stair = int(input())
stair_list = []
for _ in range(n_stair):
    stair_list.append(int(input()))

dp = [0]*n_stair
if len(stair_list)<= 2:
    print(sum(stair_list))
else:
    dp[0] = stair_list[0]
    dp[1] = stair_list[0]+ stair_list[1]
    for i in range(2, n_stair):
        # dp[i-2] : 두단계 전에서 점프한 것, d
        dp[i] = max(dp[i-3]+ stair_list[i-1], dp[i-2]) + stair_list[i]
    print(dp[-1])