def check_sosu(num):
    if num == 1 or num == 0:
        return False
    if num == 2 or num ==3:
        return True
    else:
        for item in range(2, int(num**0.5)+1):
            if (num % item) == 0:
                return False
        return True 
def permutation(cards, depth):
    # 종료 조건
    result = []
    if depth == 1:
        return cards
    else:
        for idx in range(len(cards)):
            elem = cards[idx]
            for semi_result in permutation(cards[:idx]+ cards[idx+1:], depth-1):
                result.append(elem + semi_result)
        return result
    
def solution(numbers):
    cards = list(numbers)
    print(cards)
    print(permutation(cards, 2))
    answer = 0
    result = []
    for i in range(1, len(cards)+1):
        result += list(map(int, permutation(cards,i)))
    print(list(set(result)))
    for item in list(set(result)):
        if check_sosu(item):
            answer += 1
    return answer