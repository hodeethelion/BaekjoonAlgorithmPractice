import sys
from collections import deque
input = sys.stdin.readline
r = int(input())
graph = []
for _ in range(r):
    graph.append(list(map(str, input().strip())))
    c = len(graph[0])
# r,c
visited = [[0]*c for _ in range(r)]

# for i in graph:
#     print(i)

# for i in visited:
#     print(i)

dc = [0,0,-1,1]
dr = [-1,1,0,0]

def bfs(start_r, start_c):
    q= deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1
    color = graph[start_r][start_c]

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<= next_r < r and \
               0<= next_c < c and \
               visited[next_r][next_c] == 0 and \
               graph[next_r][next_c] == color:
                q.append((next_r, next_c))
                visited[next_r][next_c] = 1
    return color

pic = []
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            pic.append(bfs(i,j))
# print(pic)

print(len(pic), end =' ')
visited = [[0]*c for _ in range(r)]

def bfs_2(start_r, start_c):
    q= deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1
    color = graph[start_r][start_c]

    if color == 'R' or color == 'G':
        while q:
            cur_r, cur_c = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if 0<= next_r < r and \
                0<= next_c < c and \
                visited[next_r][next_c] == 0 and \
                graph[next_r][next_c] in {'R', 'G'}:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = 1
        return color
    else:
        while q:
            cur_r, cur_c = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if 0<= next_r < r and \
                0<= next_c < c and \
                visited[next_r][next_c] == 0 and \
                graph[next_r][next_c] == color:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = 1
        return color
    
pic = []
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            pic.append(bfs_2(i,j))
print(len(pic))

    



# 큐에서 영역찾기
# 색맹은 R이랑 G는 상관없다고 봄
