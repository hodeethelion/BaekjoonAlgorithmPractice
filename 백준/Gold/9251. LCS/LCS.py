import sys
input = sys.stdin.readline
str1 =  str(input().strip())
str2 =  str(input().strip())
r = len(str1)
c = len(str2)
cache = [[0]* (c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        if str1[i-1] == str2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i-1][j], cache[i][j-1]) 
print(cache[-1][-1])
