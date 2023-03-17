import sys
sys.setrecursionlimit(10**6)
n_point, n_line = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(n_point + 1)]

for _ in range(n_line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for item in graph:
    item.sort()
visited = [False] * (n_point + 1)
count = 1

def dfs(graph, start):
    global count
    global visited
    visited[start] = True
    # print(start, ' visited!')
    for item in graph[start]:
        if not visited[item]:
            dfs(graph, item)
dfs_count = 0
visited = [False] * (n_point + 1)

for index in range(1, len(visited)):
    if visited[index] == False:
        dfs(graph, index)
        # print('linked over! ')
        dfs_count += 1
        # print(visited)
    else:
        pass
print(dfs_count)