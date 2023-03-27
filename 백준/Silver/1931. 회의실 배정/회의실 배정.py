import sys
input = sys.stdin.readline
num = int(input())
meetings = []

for _ in range(num):
    a, b = map(int, input().split())
    meetings.append([a,b])
# print(meetings)
# meetings.sort(key=)
meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = meetings[0][1]
for i in range(1, num):
    if meetings[i][0] >= end_time:
        cnt+=1
        end_time = meetings[i][1]
print(cnt)