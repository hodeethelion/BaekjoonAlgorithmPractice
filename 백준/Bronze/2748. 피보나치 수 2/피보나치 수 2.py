import sys
input = sys.stdin.readline
def fibo(n):
    list_1 = [0 for _ in range(n+1)]
    list_1[1] = 1
    for i in range(1, n):
        list_1[i+1] = list_1[i] + list_1[i-1]
    return list_1[-1]
n = int(input())
print(fibo(n))