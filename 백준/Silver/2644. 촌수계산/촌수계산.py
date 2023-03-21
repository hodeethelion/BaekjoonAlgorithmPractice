n_people = int(input())
find_a, find_b = map(int,input().split())
n_link = int(input())
graph = [[] for _ in range(n_people+1)]

for _ in range(n_link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
import sys
sys.setrecursionlimit(10**6)

visited = [False for _ in range(n_people+1)] 

def dfs(start, count):
    global find_b
    visited[start] = True
    if start == find_b:
        print(count)
        sys.exit(0)
    for item in graph[start]:
        if not visited[item]:
            dfs(item, count+1)
dfs(find_a, 0)
print(-1)