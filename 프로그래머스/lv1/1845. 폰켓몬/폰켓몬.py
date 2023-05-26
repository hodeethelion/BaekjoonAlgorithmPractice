def solution(nums):
    answer = 0
    choose = int(len(nums)/2 )
    nums = list(set(nums))
    
    return min(choose, len(nums))