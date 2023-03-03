#X보다 작은 수
sample, standard = map(int,input().split())
비교_list = list(map(int, input().split()))
ans_list= []

for i in range(sample):
    if standard > 비교_list[i]:
        ans_list.append(비교_list[i])
print(*ans_list)