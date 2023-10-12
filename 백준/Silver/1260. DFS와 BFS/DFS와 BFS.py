from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for idx in range(n+1):
    graph[idx].sort()

visited = [False for _ in range(n+1)]
ans = []
def dfs(start_point):
    visited[start_point] = True
    ans.append(start_point)
    for item in graph[start_point]:
        if visited[item] == False:
            dfs(item)
    else:
        return

dfs(start)
ans = list(map(str, ans))
print(' '.join(ans))

visited = [False for _ in range(n+1)]
ans = []

def bfs(start_point):
    q = deque([start_point])
    visited[start_point] = True
    ans.append(start_point)
    while q:
        next = q.popleft()
        for item in graph[next]:
            if visited[item] == False:
                ans.append(item)
                q.append(item)
                visited[item] = True
bfs(start)
ans = list(map(str, ans))
print(' '.join(ans))