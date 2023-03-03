## 종이  자르기
g, s = [int(i) for i in input().split()]
cut_num = int(input())
ga = 0
sae = 1
ga_list = [0]
sae_list = [0]
ga_list.append(g)
sae_list.append(s)


for _ in range(cut_num):
    direc, spot = map(int, input().split())
    if direc == 0:
        sae_list.append(spot)
    else:
        ga_list.append(spot)
ga_list = sorted(ga_list) 
sae_list = sorted(sae_list)
def getDiff(list):
    ga_diff = []
    for i in range(len(list)-1):
        ga_diff.append(list[i+1]-list[i])
    return ga_diff
        
ga_list2 = getDiff(ga_list)
sae_list2 = getDiff(sae_list)
size_list = []
for i in ga_list2:
    for j in sae_list2:
        size_list.append(i*j)
print(max(size_list))