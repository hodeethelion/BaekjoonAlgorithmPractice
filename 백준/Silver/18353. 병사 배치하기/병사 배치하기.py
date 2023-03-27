import sys
input = sys.stdin.readline
n_soldier = int(input())
soldier_list = list(map(int, input().split()))
# print(n_soldier, soldier_list)
soldier_list = soldier_list[::-1]
# print(soldier_list)


dp = [1] * (n_soldier)
for i in range(1, n_soldier):
    for j in range(i):
        if soldier_list[i] > soldier_list[j]:
            dp[i] = max(dp[j]+1, dp[i])
    # print(dp)
print(n_soldier - max(dp))