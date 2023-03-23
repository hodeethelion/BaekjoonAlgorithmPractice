import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
# for i in graph:
#     print(i)

dr= [-1,1,0,0]
dc= [0,0,-1,1]
visited = [[0]* n for _ in range(n)]
# print(visited)
count = 0

def bfs(start_r, start_c):
    global count
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1
    count += 1
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<= next_r <n and \
               0<= next_c <n and \
               visited[next_r][next_c] == 0 and\
               graph[next_r][next_c] == 1:
                count+=1
                # print(count)
                visited[next_r][next_c] = 1 
                q.append((next_r, next_c))
    return count
ans_list= []
for i in range(n):
    for j in range(n):
        if visited[i][j]== 0 and graph[i][j] ==1:
            count = 0
            ans_list.append(bfs(i,j))
# print(ans_list)
ans_list.sort()
print(len(ans_list))
for i in ans_list:
    print(i)