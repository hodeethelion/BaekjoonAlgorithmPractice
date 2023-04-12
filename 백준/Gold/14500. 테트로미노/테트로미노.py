import sys
input = sys.stdin.readline
#그래프에서 한 점을 중심으로 가장
row, col = map(int, input().split())
graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))

visited = [[0]* col for _ in range(row)] 
dc = [-1,1,0,0]
dr = [0,0,-1,1]
maxi = 0

def dfs(graph, start, block, cur_sum):
    global maxi, row, col
    if block == 0: 
        cur_sum+= graph[start[0]][start[1]]
    if block == 3:
        maxi = max(cur_sum, maxi)
        return
    for direction in range(4):
        new_r = start[0] + dr[direction]
        new_c = start[1] + dc[direction] 
        if 0<= new_r < row and 0<= new_c < col \
            and visited[new_r][new_c] == 0:
            if block == 1:
                visited[new_r][new_c] = 1
                dfs(graph, start, block+1, cur_sum+ graph[new_r][new_c])
                visited[new_r][new_c] = 0
            visited[new_r][new_c] = 1
            dfs(graph, (new_r, new_c), block+1, cur_sum+ graph[new_r][new_c])
            visited[new_r][new_c] = 0
            
for i in range(row):
    for j in range(col):
        visited[i][j] = 1
        dfs(graph, (i,j), 0, 0)
        visited[i][j] = 0
        
print(maxi)