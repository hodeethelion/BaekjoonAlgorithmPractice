import sys
from collections import deque
input = sys.stdin.readline
n_case = int(input())

for _ in range(n_case):
    c, r, n_batchu = map(int, input().split())
    graph_batchu = [[0]*c for _ in range(r)]
    # print(r, c)
    for _ in range(n_batchu):
        col, row = map(int, input().split())
        graph_batchu[row][col] = 1
    dc = [0,0,-1,1]
    dr = [-1,1,0,0]

    # for i in graph_batchu:
    #     print(i)

    def bfs(start_r, start_c):
        # print('yala')
        graph_batchu[start_r][start_c] = 0
        q = deque()
        q.append((start_r, start_c))
        
        while q:
            cur_r, cur_c = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]

                if 0<= next_r < r and \
                0<= next_c < c and \
                graph_batchu[next_r][next_c] == 1:
                    graph_batchu[next_r][next_c] = 0
                    q.append((next_r, next_c))
        return True
    
    count = 0
    for i in range(0, r):
        # print(i)
        for j in range(0, c):
            # print(j)
            if graph_batchu[i][j]==1:
                bfs(i,j)
                count+=1 
    print(count)