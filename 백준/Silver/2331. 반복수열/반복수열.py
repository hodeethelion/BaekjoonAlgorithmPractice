a, p = map(int, input().split())
connect_list = [str(a)]

def make_next(k : str, p : int):
    sample = list(k)
    total = 0
    for item in sample:
        total += pow(int(item), p)
    return str(total)

while True:
    next = make_next(connect_list[-1], p)
    try:
        ans = connect_list.index(next)
        break
    except ValueError:
        connect_list.append(next)

print(ans)