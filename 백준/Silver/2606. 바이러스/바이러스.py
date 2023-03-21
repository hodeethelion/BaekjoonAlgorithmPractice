import sys
input = sys.stdin.readline
n_computer = int(input())
n_line = int(input())
graph = [[] for _ in range(n_computer+1)]
for _ in range(n_line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n_computer+1)

infected = []
def dfs(graph, start, visited):
    visited[start] = True
    for item in graph[start]:
        if visited[item] == False:
            infected.append(item)
            # visited[item] = True
            dfs(graph, item, visited)
dfs(graph,1,visited)
print(len(infected))