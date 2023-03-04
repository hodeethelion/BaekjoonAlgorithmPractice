run_num = int(input())
def is_sosu(num):
    if num == 1:
        return False
    else:
        for divider in range(2, num):
            if (num % divider) != 0:
                continue
            else:
                return False
        return True
for i in range(run_num):
    case = int(input())
    for small in range(case//2, 0, -1):
        big = case - small
        if is_sosu(big) & is_sosu(small):
            print(small,big)
            break