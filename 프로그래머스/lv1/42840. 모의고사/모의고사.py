def solution(answers):
    #1번 수포자 12345 / 12345 
    #2번 수포자 21232425 / 
    #3번 수포자 3311224455 / 
    answer = []
    char1 = [1,2,3,4,5]
    char2 = [2,1,2,3,2,4,2,5]
    char3 = [3,3,1,1,2,2,4,4,5,5]
    count1, count2, count3 = 0, 0, 0
    print(answers)
    for idx, ans in enumerate(answers):
        print("idx" , idx)
        if ans == char1[idx % len(char1)]:
            count1 += 1
        if ans == char2[idx % len(char2)]:
            count2 += 1 
        if ans == char3[idx % len(char3)]:
            count3 += 1 
    print(count1, count2, count3)
    max_score= max(count1, count2, count3)
    print(max_score)
    if count1 == max_score:
        answer.append(1)
    if count2 == max_score:
        answer.append(2)
    if count3 == max_score:
        answer.append(3)
    return answer