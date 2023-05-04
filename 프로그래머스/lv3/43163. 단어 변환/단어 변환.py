from collections import deque
def candidate(word1, word2):
    count = 0
    for idx, item in enumerate(word1):
        if word2[idx] == item:
            continue
        else:
            count += 1
    if count==1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [0 for _ in range(len(words))]
    
    while q: 
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        else:
            for i, n_word in enumerate(words):
                print(n_word)
                if V[i] == 0 and candidate(word, n_word):
                    V[i] = 1
                    q.append([n_word, cnt+1])
    
    print(answer)
    
    return answer