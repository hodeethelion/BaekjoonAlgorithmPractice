def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    for idx, item in enumerate(citations):
        h_index = idx + 1
        count = 0
        for num in citations:
            if num >= h_index:
                count += 1 
            else:
                continue
        if count >= h_index:
            answer = h_index
        else:
            break
    return answer