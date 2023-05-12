def solution(sizes):
    new_sizes = []
    for item in sizes:
        new_sizes.append(sorted(item, reverse= True))
    a = 0
    b = 0
    for size in new_sizes:
        a = max(size[0], a)
        b = max(size[1], b)
    return a*b