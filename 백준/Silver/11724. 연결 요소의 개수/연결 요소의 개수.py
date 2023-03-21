import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n_point, n_line = map(int, input().split())
graph = [[] for _ in range(n_point+1)]
for _ in range(n_line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n_point +1)


def dfs(graph, start, visited):
    if visited[start] == False:
        visited[start] = True
    # else:
    #     return
    for item in graph[start]:
        if visited[item] == False:
            visited[item] = True
            dfs(graph, item, visited)
    return True

count = 0
for i in range(1, n_point+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        count += 1 
print(count)