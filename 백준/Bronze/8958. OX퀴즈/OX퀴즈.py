for _ in range(int(input())):
    score = 0
    sample = input().split('X')
    for i in sample:
        score += sum(range(len(i)+1))
    print(score)