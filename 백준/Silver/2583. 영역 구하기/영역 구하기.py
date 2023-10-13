from collections import deque
row, col, n_rec = map(int, input().split())
graph = [[0 for _ in range(col)] for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]

for _ in range(n_rec):
    col_1, row_1, col_2, row_2 = map(int, input().split())
    for i in range(row-row_2, row - row_1):
        for j in range(col_1, col_2):
            graph[i][j] = 1

def in_range(x, y):
    return 0 <= x and x < row and 0 <= y and y < col

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    count = 1
    while q:
        c_r, c_c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = c_r + dr, c_c + dc
            if in_range(nr, nc) and visited[nr][nc] == 0 and graph[nr][nc] == 0:
                count += 1
                q.append([nr, nc])
                visited[nr][nc] = 1
    return count

ans_list = []
for i in range(row):
    for j in range(col):
        if visited[i][j] == 0 and graph[i][j] == 0:
            ans = bfs(i, j)
            ans_list.append(ans)
ans_list.sort()
print(len(ans_list))
print(' '.join(list(map(str, ans_list))))
