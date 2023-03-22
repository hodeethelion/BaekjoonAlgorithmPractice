#SETTINGS
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 
n_vertex = int(input())
in_out = 'S' + str(input().strip())
#'10111'
graph = [[] for _ in range(n_vertex+1)]
for _ in range(n_vertex-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
count = 0
def dfs(start, graph, visited):
    global count
    visited[start] = True
    for item in graph[start]:
        # 외부면
        if visited[item] == False:
            if in_out[item] == '1':
                count+=1
            
         # 내부면
            elif in_out[item] == '0':
                dfs(item, graph, visited)

for i in range(1, n_vertex+1):
    visited = [False] * (n_vertex+1)
    if in_out[i] == '1':
        dfs(i,graph,visited)
print(count)