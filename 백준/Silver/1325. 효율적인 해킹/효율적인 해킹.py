import sys
from collections import deque
n_computer, n_lines = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n_computer+1)]
for _ in range(n_lines):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
visited = [False] * (n_computer + 1)

infected_list = [0] * (n_computer + 1)

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    infected = 1
    
    while q:
        now = q.popleft()
        for next_computer in graph[now]:
            if not visited[next_computer]:
                q.append(next_computer)
                infected += 1
                visited[next_computer] = True
                infected_list[start] = infected

for i in range(1, n_computer+1):
    visited = [False] * (n_computer + 1)
    bfs(i)
    
for index in range(1, n_computer+1):
    if infected_list[index] == max(infected_list):
        print(index)