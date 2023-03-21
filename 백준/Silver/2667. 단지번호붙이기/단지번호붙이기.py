#BFS
from collections import deque
import sys

n = int(input())
graph = [ ]
for _ in range(n):
    graph.append(list(map(int, input())))
# print(n)
# print(graph)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[0]* n for _ in range(n)]
ans = []
def bfs(row, col):
    q = deque()
    if visited[row][col] == 1:
        return
    if visited[row][col] == 0:
        visited[row][col] = 1
        # 큐 세팅
        q.append((row, col))
        town = 1
        while q:
            cur_row, cur_col = q.popleft()
            for i in range(4):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]
                if 0<=next_row <n and 0<=next_col <n and \
                    visited[next_row][next_col] == 0 and \
                    graph[next_row][next_col] == 1:
                    visited[next_row][next_col] = 1 
                    q.append((next_row, next_col))
                    town += 1
    return town


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            k = bfs(i, j)
            if k == None or k == 0:
                continue
            else:
                ans.append(k)
ans.sort()
print(len(ans))
for i in ans:
    print(i)