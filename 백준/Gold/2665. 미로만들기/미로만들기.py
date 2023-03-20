from collections import deque
import sys

# input 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[0]*n for _ in range(n)]

dc = [0,0,-1,1]
dr = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[-1]*n for _ in range(n)]
    visited[0][0] = 0
    while q:
        cur_row, cur_col  = q.popleft()
        if cur_row == n-1 and cur_col == n-1:
            return visited[cur_row][cur_col]
        for i in range(4):
            next_row = cur_row + dr[i]
            next_col = cur_col + dc[i]
            if 0<= next_row < n and \
               0<= next_col < n and \
               visited[next_row][next_col] == -1:
                if graph[next_row][next_col] == 1:
                    q.appendleft((next_row, next_col))
                    visited[next_row][next_col] = visited[cur_row][cur_col]
                else:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = visited[cur_row][cur_col] +1
print(bfs())