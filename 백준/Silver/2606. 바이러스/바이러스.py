import sys
sys.setrecursionlimit(10**6)
n_computer = int(input())
n_link = int(input())
graph = [[] for i in range(n_computer+1)]

for _ in range(n_link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for item in graph:
    item.sort()

visited = [False] * (n_computer + 1)
visit_computer = []
def dfs(graph, start, visited):
    visited[start] = True
    visit_computer.append(start)
    for item in graph[start]:
        if not visited[item]:
            dfs(graph, item, visited)
dfs(graph,1,visited)
print(len(visit_computer)-1)