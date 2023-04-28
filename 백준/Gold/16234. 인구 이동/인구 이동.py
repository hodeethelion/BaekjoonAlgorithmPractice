import sys
from collections import deque
input = sys.stdin.readline
n_len, min_dif, max_dif = map(int, input().split())
map_countries = []
for _ in range(n_len):
    map_countries.append(list(map(int, input().split())))

# print(n_len, min_dif, max_dif)
# for i in map_countries:
#     print(i)
dx_l = [-1,1,0,0]
dy_l = [0,0,-1,1]

def bfs(x,y):
    global dx_l, dy_l
    q = deque()
    q.append((x,y))
    union_contry = []
    union_contry.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = dx_l[i]
            dy = dy_l[i]
            nx = x + dx
            ny = y + dy
            if 0<= nx< n_len and 0<= ny < n_len and not visited[nx][ny]:
                if min_dif <= abs( map_countries[x][y] - map_countries[nx][ny]) <= max_dif:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union_contry.append((nx,ny))
    return union_contry

day_count = 0 
while True:
    visited = [[False]*n_len for _ in range(n_len)]
    move = False 
    for i in range(n_len):
        for j in range(n_len):
            if not visited[i][j]:
                visited[i][j] = True
                union_country = bfs(i,j)
                if 1< len(union_country):
                    move = True
                    moved_people = sum([map_countries[x][y] for x, y in union_country]) // len(union_country)
                    for x, y in union_country:
                        map_countries[x][y] = moved_people
    if move == False:
        break
    else:
        day_count +=1 
print(day_count)