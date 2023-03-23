import sys
a = int(sys.stdin.readline())
def tile(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        n_list = [0 for _ in range(num+1)]
        n_list[1] = 1
        n_list[2] = 2 
        for i in range(2, num):
            n_list[i+1] = (n_list[i] + n_list[i-1]) % 10007
    return n_list[num]

print(tile(a))