def solution(word):
    answer = 0
    # 781 156 31 6 1
    adding = [781, 156, 31, 6, 1]
    index_alpha = ["A", "E", "I", "O", "U"]
    length = len(word)
    answer += length
    for i in range(0, 5):
        try:
            if word[i] == "E":
                answer += adding[i] * 1
            if word[i] == "I":
                answer += adding[i] * 2
            if word[i] == "O":
                answer += adding[i] * 3
            if word[i] == "U":
                answer += adding[i] * 4
        except:
            break
        
    return answer