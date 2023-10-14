import sys
from collections import deque
input = sys.stdin.readline
col, row = map(int, input().split())
farm = []
q = deque()
for i in range(row):
    to_add = list(map(int, input().split()))
    for j in range(col):
        if to_add[j] == 1:
            q.append([i, j])
    farm.append(to_add)

drs = [-1, 1, 0, 0]
dcs = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x and x < row and 0 <= y and y < col

def bfs(row, col, farm):
    count = -1
    # 1인 것만 deque에 담았으므로 그것만 실행
    while q:
        count += 1
        for _ in range(len(q)):
            c_r, c_c = q.popleft()
            for dr, dc in zip(drs, dcs):
                n_r, n_c = c_r + dr, c_c + dc
                if in_range(n_r, n_c) and farm[n_r][n_c] == 0:
                    farm[n_r][n_c] = 1
                    q.append([n_r, n_c])
    for one_line in farm:
        if 0 in one_line:
            return -1
    return count
answer = bfs(row, col, farm)
print(answer)