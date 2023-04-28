n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(n)
# print(graph)

for i in range(n): # 거치는 점 
    for j in range(n): # 시작점
        for k in range(n): # 끝점
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
# print(graph)
for i in graph:
    for k in i:
        print(k, end=' ')
    print()