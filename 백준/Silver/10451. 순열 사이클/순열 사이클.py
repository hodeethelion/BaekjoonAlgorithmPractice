T = int(input())
def dfs(start):
    visited[start] = True
    for item in graph[start]:
        if not visited[item]:
            dfs(item)
        else:
            continue


for test_case in range(1, T+1):
    count = 0
    N = int(input())
    ordered_num = list(range(1, N+1))
    num_list = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for idx in range(N):
        graph[ordered_num[idx]].append(num_list[idx])
    visited = [False for _ in range(N+1)]
    for idx in range(1, N+1):
        if not visited[idx]:
            dfs(idx)
            count += 1
    print(count)