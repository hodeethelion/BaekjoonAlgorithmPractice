from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# 상 하 좌 우
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]

def in_range(row, col):
    return 0 <= row and row < n and 0 <= col and col < m

def bfs(r, c, z):
    q = deque()
    q.append([r, c, z])
    while q:
        row, col, z = q.popleft()
        if row == n - 1 and col == m - 1:
            return visited[row][col][z]
        for dr, dc in zip(drs, dcs):
            nr = dr + row
            nc = dc + col
            # 1. 이동할 곳이 벽인 경우
            if in_range(nr, nc) and graph[nr][nc] == 1 and z == 0:
                visited[nr][nc][1] = visited[row][col][0] + 1
                q.append([nr, nc, 1])
            # 2. 이동할 곳이 벽이 아닌 경우
            elif in_range(nr, nc) and graph[nr][nc] == 0 and visited[nr][nc][z] == 0:
                visited[nr][nc][z] = visited[row][col][z] + 1
                q.append([nr, nc, z])
    return -1
print(bfs(0, 0, 0))