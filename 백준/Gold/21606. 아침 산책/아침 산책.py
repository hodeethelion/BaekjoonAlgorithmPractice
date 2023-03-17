##### SAMPLE

# DATA inputs
import sys
n_place = int(sys.stdin.readline())
in_out = 'k' + str(sys.stdin.readline().strip())
graph = [[] for _ in range(n_place + 1)]

for _ in range(n_place -1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for item in graph:
    item.sort()


# graph는 세팅 되어있으니까
visited = [False for _ in range(n_place+1)]

# 만약 외부에 있으면 dfs 자체를 하지마

def dfs(start, visited):
    global count
    visited[start] = True
    # print('start: ', start, end = '  ')
    # graph에 연결된 모든 아이템들
    for item in graph[start]:
        # print('going: ', item)
        # 아이템을 방문하지 않았다면
        if not visited[item]:
            # 아이템을 체크 만약 내부면 +1
            if in_out[item] == '1':
                count += 1
                # print('start', start,item, 'finished')
            # 아이템이 만약 외부면 
            elif in_out[item] == '0':
                dfs(item, visited)
    return

total = 0
for test_index in range(1,n_place +1):
    count = 0
    if in_out[test_index] != '0':
        dfs(test_index, [False for _ in range(n_place+1)])
        total += count
print(total)