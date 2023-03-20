from collections import deque
from sys import stdin

n_city, n_road, n_length, start = map(int, stdin.readline().split())
graph = [[] for _ in range(n_city+1)]
distance = [0] * (n_city+1)
visited = [False] * (n_city+1)
# print(distance)

for _ in range(n_road):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

######## SETTING ##########    
###########################    
# print('distance : ', distance)
# print('graph : ' , graph)
# print('visited : ', visited)

    
def bfs(start_num):
    # answer에다가 담기
    answer = []
    # queue에 시작값을 넣기
    q = deque([start_num])
    # 처음 밟은 거니까 True! 
    visited[start_num] = True
    # 
    distance[start_num] = 0
    while q:
        now = q.popleft()
        # 가장 마지막에 넣은 것을 
        for next_index in graph[now]:
            # 갈 수 있는 곳 하나 하나 해보기 
            if not visited[next_index]:
                visited[next_index] = True
                q.append(next_index)
                distance[next_index] = distance[now] + 1
                
                # 답일 경우에만~ 
                if distance[next_index] == n_length:
                    answer.append(next_index)
                    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)
            
bfs(start)