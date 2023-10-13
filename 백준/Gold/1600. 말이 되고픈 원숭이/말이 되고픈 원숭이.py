from collections import deque
k = int(input())
col, row = map(int, input().split())
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))
visited = [[[0 for _ in range(k+1)] for _ in range(col)] for _ in range(row)]

drs = [-1, 1, 0, 0]
dcs = [0, 0, 1, -1]
drs_horse = [2, 2, 1, 1, -1, -1, -2, -2]
dcs_horse = [1, -1, 2, -2, 2, -2, 1, -1]

def in_range(x, y):
    return 0 <= x and x < row and 0 <= y and y < col

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        c_r, c_c, z = q.popleft()

        # 목표 지점에 도달 하면
        if c_r == row - 1 and c_c == col -1:
            return visited[c_r][c_c][z] - 1

        # 상하좌우로 이동
        for dr, dc in zip(drs, dcs):
            nr, nc = c_r + dr, c_c + dc
            if in_range(nr, nc) and visited[nr][nc][z] == 0 and graph[nr][nc] == 0:
                visited[nr][nc][z] = visited[c_r][c_c][z] + 1
                q.append([nr, nc, z])
        # 말로 이동
        if z < k:
            for dc_horse, dr_horse in zip(dcs_horse, drs_horse):
                nr, nc = dr_horse + c_r, dc_horse + c_c
                if in_range(nr, nc) and graph[nr][nc] == 0 and visited[nr][nc][z+1] == 0:
                    visited[nr][nc][z+1] = visited[c_r][c_c][z] + 1
                    q.append([nr, nc, z+1])
    return -1


print(bfs())
