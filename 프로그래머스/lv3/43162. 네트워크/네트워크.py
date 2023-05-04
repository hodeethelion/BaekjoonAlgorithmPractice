def solution(n, computers):
    visited = [0] * n
    
    def dfs(start):
        if visited[start] == 1:
            return
        elif visited[start] == 0:
            visited[start] = 1
            for idx, item in enumerate(computers[start]):
                if item == 1 and visited[idx] == 0:
                    dfs(idx)
    answer = 0
    for index in range(n):
        if visited[index] == 0:
            dfs(index)
            answer += 1

    return answer