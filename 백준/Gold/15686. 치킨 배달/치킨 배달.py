import sys
from itertools import combinations
input = sys.stdin.readline
# 0은 빈칸 1 은 집 2는 치킨 집 
# 먼저 생각한게 dfs로 치킨 집을 찾는다. combination으로 치킨 집을 찾는다 --> 너무 경우의 수가 많? 
# 두번째 
# 먼저 잡기
n_graph, max_chcicken = map(int, input().split())
graph = []
for _ in range(n_graph):
    graph.append(list(map(int, input().split())))

# combination으로 잡기
home_list = []
chickenhome_list = []

for i in range(n_graph):
    for j in range(n_graph):
        if graph[i][j]==0:
            continue
        elif graph[i][j] == 1:
            home_list.append((i,j))
        elif graph[i][j] == 2:
            chickenhome_list.append((i,j))

combo_list = combinations(chickenhome_list, max_chcicken)

ans = sys.maxsize
for combi in combo_list:
    total_chicken = 0
    for home in home_list:
        min_chicken= sys.maxsize
        for chicken_house in combi:
            min_chicken = min(min_chicken, abs(home[0]- chicken_house[0]) + abs(home[1]- chicken_house[1]))
        total_chicken+= min_chicken
    ans = min(total_chicken, ans)
print(ans)

        