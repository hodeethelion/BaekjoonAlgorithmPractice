import sys
input = sys.stdin.readline
n_people = int(input())
n_list = int(input())
graph=[ [] for _ in range(n_people+1) ]
for _ in range(n_list):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited = [0] * (n_people+1)

def dfs(start, depth):
    if depth == 2:
        return
    # print(graph[start])
    for i in graph[start]:
        
        visited[i] = 1
        dfs(i, depth+1)
            # visited[i] = 1
        # print('going' , i, 'depth ', depth)

dfs(1, 0)
# print(visited)
if visited[1]==0:
    print(sum(visited))
else:
    print(sum(visited)-1)