from collections import deque
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, list(input().rstrip()))))
visited = [[[0, 0] for _ in range(c)] for _ in range(r)]
visited[0][0][0] = 1

dcs = [-1, 1, 0, 0]
drs = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < r and 0<= y and y < c

def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        c_r, c_c, z = q.popleft()

        if c_r == r - 1 and c_c == c - 1:
            return visited[c_r][c_c][z]

        for dc, dr in zip(dcs, drs):
            nc, nr = c_c + dc, c_r + dr
            # 1. 벽을 만나서 부셔야 하는 상황이라면
            if in_range(nr, nc) and graph[nr][nc] == 1 and visited[nr][nc][z] == 0 and z == 0:
                visited[nr][nc][1] = visited[c_r][c_c][0] + 1
                q.append([nr, nc, 1])
            # 2. 벽을 안만나서 그냥 지나갈 수 있는 상황이라면
            elif in_range(nr, nc) and visited[nr][nc][z] == 0 and graph[nr][nc] == 0:
                visited[nr][nc][z] = visited[c_r][c_c][z] + 1
                q.append([nr, nc, z])
    return -1
print(bfs())