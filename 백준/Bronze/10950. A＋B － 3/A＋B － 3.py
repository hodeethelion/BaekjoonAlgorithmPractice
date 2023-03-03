# 몇줄을 받을 건지 나온다
a = int(input())
for i in range(a):
    a, b = map(int, input().split())
    print(a + b)