import sys
from collections import deque

# input 받기 
r, c = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, sys.stdin.readline().strip())))
# print(graph)

#BFS setting
visited = [[0] * c for _ in range(r)]
# print(visited)
ans = [0, 0]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

#BFS
def bfs(row, col):
    #1. que setting
    q = deque()
    q.append((row, col))
    #2. visit setting
    visited[row][col] = 1
    sheep, wolf = 0, 0
    if graph[row][col] == 'v':
        wolf += 1
    if graph[row][col] == 'o':
        sheep += 1

    while q:
        cur_row, cur_col = q.popleft()

        for i in range(4):
            next_row = cur_row + dr[i]
            next_col = cur_col + dc[i]
            if 0<= next_row< r and 0<= next_col<c and visited[next_row][next_col] == 0 \
            and graph[next_row][next_col]!= '#':
                if graph[next_row][next_col] == 'v':
                    wolf += 1
                if graph[next_row][next_col] == 'o':
                    sheep += 1
                q.append((next_row, next_col))
                visited[next_row][next_col] = 1
        
    if sheep <= wolf:
        ans[1] += wolf
    if wolf < sheep:
        ans[0] += sheep


for i in range(r):
    for j in range(c):
        if visited[i][j] != 1 and graph[i][j]!= '#':
            bfs(i,j)
print(*ans)