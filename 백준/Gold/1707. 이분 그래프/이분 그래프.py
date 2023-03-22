import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n_test = int(input())


# 데이터 저장을 visited에다가 하는 방식
def dfs(start, group):
    visited[start] = group
    for item in graph[start]:
        if visited[item] == group:
            return False
        elif visited[item] == -group:
            continue
        else:
            next_stage = dfs(item, -group)
            if next_stage == False:
                return False
            else:
                continue
    return True

for _ in range(n_test):
    n_vertex, n_line = map(int, input().split())
    graph = [[] for _ in range(n_vertex+1)]
    for _ in range(n_line):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (n_vertex+1)
    ans = True

    for sample in range(1, n_vertex+1):
        if visited[sample] == 0:
            ans = dfs(sample, 1)
            if ans == False:
                break
            else:
                continue
    if ans== False: 
        print('NO')
    else: 
        print('YES')

        