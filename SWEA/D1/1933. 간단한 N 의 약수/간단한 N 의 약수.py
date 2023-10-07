a = int(input())
ans_list = []
for idx in range(1,a+1):
    if (a%idx) ==0:
        ans_list.append(str(idx))
print(' '.join(ans_list))