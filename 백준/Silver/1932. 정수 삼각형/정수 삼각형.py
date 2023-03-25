import sys
input= sys.stdin.readline
n_triangle = int(input())
triangle = [[]]
for _ in range(n_triangle):
    triangle.append(list(map(int, input().split())))
# print(triangle)

# dp테이블을 똑같이 만들기
dp = [[]]
if n_triangle == 1:
    print(triangle[1][0])

if n_triangle == 2:
    dp.append([max(triangle[1])])
    dp.append([max(triangle[1])+ triangle[2][0], 
               max(triangle[1])+ triangle[2][1]])
    print(max(dp[-1]))

if n_triangle >= 3:
    dp.append([max(triangle[1])])
    dp.append([max(triangle[1])+ triangle[2][0], 
               max(triangle[1])+ triangle[2][1]])
    for i in range(3, n_triangle+1):
        for j in range(i):
#            print(j)
            if j == 0:
                dp.append([dp[i-1][j]+ triangle[i][0]])
            elif j < i-1:
                dp[i].append(
                    max( dp[i-1][j-1] ,
                        dp[i-1][j]
                         ) + triangle[i][j]
                )
            elif j == i-1:
                dp[i].append(
                    triangle[i][j]+ dp[i-1][-1]
                )

#    print(i)
    print(max(dp[-1]))