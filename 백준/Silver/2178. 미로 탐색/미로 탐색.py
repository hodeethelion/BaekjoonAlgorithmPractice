r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input())))

####### 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

###### 
from collections import deque
#start point
def bfs(start_row, start_col):
    to_go = deque()
    to_go.append((start_row, start_col))
    while to_go:
        row, col = to_go.popleft()
        for i in range(4):
            moved_row = row + drow[i]
            moved_col = col + dcol[i]
                
            if moved_col < 0 or moved_row < 0 or moved_col >= c or moved_row >= r:
                continue
                
            if graph[moved_row][moved_col] == 0:
                continue
            
            if graph[moved_row][moved_col] == 1:
                graph[moved_row][moved_col] = graph[row][col]+1
                to_go.append((moved_row, moved_col))
                # print(to_go)
                
    return graph
    
answer_graph = bfs(0,0)
print(answer_graph[-1][-1])