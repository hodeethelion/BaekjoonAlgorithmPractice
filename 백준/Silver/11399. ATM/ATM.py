import sys
input = sys.stdin.readline
n_people = int(input())
time_list = list(map(int, input().split()))
# print(n_people, time_list)

time_list.sort()
# print(n_people, time_list)

temp = 0
total = 0
for time in time_list:
    temp += time
    total += temp
print(total)