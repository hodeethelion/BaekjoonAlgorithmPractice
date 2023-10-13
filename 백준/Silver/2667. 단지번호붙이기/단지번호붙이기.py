from collections import deque

N = int(input())
map_graph = []
visit_graph = []
for _ in range(N):
    map_graph.append(list(map(int, list(input().rstrip()))))
    visit_graph.append([False for _ in range(N)])

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]
def in_range(i, j):
    return 0 <= i and i < N and 0 <= j and j < N

def can_go(i, j):
    return in_range(i, j) and visit_graph[i][j] == False and map_graph[i][j] == 1

def bfs(i, j):
    q = deque()
    q.append([i, j])
    count = 0
    while q:
        row, col = q.popleft()
        if can_go(row, col):
            count += 1
            visit_graph[row][col] = True
            for dr, dc in zip(drs, dcs):
                if can_go(dr + row, dc + col):
                    q.append([dr+row, dc + col])
    return count

ans_list = []

for r in range(N):
    for c in range(N):
        if can_go(r, c):
            ans = bfs(r, c)
            ans_list.append(ans)
ans_list.sort()
print(len(ans_list))
for i in ans_list:
    print(i)