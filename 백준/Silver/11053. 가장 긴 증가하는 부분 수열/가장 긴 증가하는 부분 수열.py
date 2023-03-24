import sys
input = sys.stdin.readline
size = int(input())
soo = list(map(int, input().split()))
# print(soo)
dp = [1]* (size)

for i in range(1, size):
    for j in range(0, i):
        if soo[i] > soo[j]:
            # print(soo[i], soo[j])
            dp[i] = max(dp[i], dp[j] + 1)
            # print(dp)
            # print()
print(max(dp))