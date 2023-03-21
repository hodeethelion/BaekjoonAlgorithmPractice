import sys
from collections import deque
input = sys.stdin.readline

n_student, n_comparison = map(int, input().split())

graph = [[] for _ in range(n_student + 1)]
degree = [0]*(n_student+1)
q = deque()

# step1. 위상만들기
for _ in range(n_comparison):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
# print(degree)
# step2. 위상이 0이라면 일단 그냥 갖다가 붙이기, 시작이니까
for i in range(1, n_student+1):
    if degree[i] == 0:
        q.append(i)
# print(q)
# print(graph)
#step3. 위상 줄여나가기
ans= []

for i in range(n_student):
    temp = q.popleft()
    ans.append(temp)

    for j in graph[temp]:
        # 위상낮추기
        degree[j] -= 1
        # 위상이 0이라면
        if degree[j] == 0:
            q.append(j)
print(*ans)
