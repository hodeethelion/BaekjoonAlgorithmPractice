def solution(numbers, target):
    # idx = 0
    target_n = len(numbers)
    ans = []
    
    def dfs(index, result):
        
        if index == target_n:
            if result == target:
                ans.append(1)
                return
            else:
                return
        else:
            dfs(index + 1, result + numbers[index])
            dfs(index + 1, result - numbers[index])
    
    dfs(0, 0)
    return sum(ans)