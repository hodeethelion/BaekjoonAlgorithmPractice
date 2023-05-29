def solution(lottos, win_nums):
    unknown = 0
    score = 0
    for item in lottos:
        if item == 0:
            unknown += 1
        else:
            if item in win_nums:
                score += 1
    # print(score, unknown)
    least = score
    best = score + unknown
    print(least, best)
    prize = [6,6,5,4,3,2,1]
    answer = [prize[best], prize[least]]
    return answer