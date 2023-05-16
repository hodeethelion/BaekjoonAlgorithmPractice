def solution(brown, yellow):
    total = brown + yellow
    for col in range(1, total//2):
        if total % col == 0:
            row = total // col
            if (total - 2*(row+col) + 4) == yellow:
                break
    print("ans! row, col ",(row,col))
    
    answer = [row, col]
    return answer