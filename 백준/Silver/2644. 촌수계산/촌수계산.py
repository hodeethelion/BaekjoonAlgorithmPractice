import sys
input = sys.stdin.readline
n_people = int(input())
start_p , end_p = map(int, input().split())
n_line = int(input())
graph= [[] for _ in range(n_people+1)]
for _ in range(n_line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

sys.setrecursionlimit(10**6)

visited = [0] * (n_people + 1)
ans = []

def dfs(start, count):
    global end_p
    # print(start)
    visited[start] = 1
    if start == end_p:
        ans.append(count)
        # print('yala')
        return
    for item in graph[start]:
        # print(item)
        if visited[item] == 0:
            visited[item] = 1
            dfs(item, count+1)

dfs(start_p, 0)
try:
    print(min(ans))
except:
    print(-1)