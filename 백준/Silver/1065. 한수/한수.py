a = int(input())

def is_hansu(k):
    if k<100:
        return 1
    else:
        sam = [i for i in str(k)]
        gangeok = []
        for k in range(len(sam)-1):
            g = int(sam[k]) - int(sam[k+1])
            gangeok.append(g)
            check = set(gangeok)
        if len(check) == 1:
            return 1
        else:
            return 0
count = 0
for i in range(1, a+1):
    count += is_hansu(i)
print(count)