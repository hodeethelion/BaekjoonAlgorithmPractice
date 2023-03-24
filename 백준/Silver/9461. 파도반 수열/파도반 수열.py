import sys
input = sys.stdin.readline
test_case = int(input())

def padoban(number):
    n_list = [0 for _ in range(101)]
    n_list[1] = 1;n_list[2] = 1;n_list[3] = 1
    n_list[4] = 2;n_list[5] = 2;n_list[6] = 3
    n_list[7] = 4;n_list[8] = 5;n_list[9] = 7
    for i in range(10, number+1):
        n_list[i] = n_list[i-1] + n_list[i-5]
    return n_list[number]
for _ in range(test_case):
    num = int(input())
    print(padoban(num))
