# BFS와 DFS
import sys
from collections import deque
n_point, n_line, start = map(int, input().split())
graph = [[] for i in range(n_point+1)]

# 그래프 채우기
for _ in range(n_line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for item in graph:
    item.sort()

#DFS 
visited = [False] * (n_point+1)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for item in graph[start]:
        if not visited[item]:
            dfs(graph, item, visited)
    
dfs(graph, start, visited)

print()
#BFS
visited = [False] * (n_point+1)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end= ' ')
        for item in graph[v]:
            if not visited[item]:
                que.append(item)
                visited[item] = True


bfs(graph, start, visited)