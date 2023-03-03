for _ in range(int(input())):
    d = [int(x) for x in input().split()]
    over = 0
    person = d[0]
    scores = d[1:] 
    mean = (sum(scores)/ person) 
    for score in scores:
            if score > mean:
                over += 1
    perc = round(over/len(scores)*100, 3)
    print(str(format(perc,'.3f'))+"%")