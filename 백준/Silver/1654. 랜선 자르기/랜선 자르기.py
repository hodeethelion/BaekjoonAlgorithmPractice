import sys
input = sys.stdin.readline
n_lan, necess_lan = map(int, input().split())
lans = []
for _ in range(n_lan):
    lans.append(int(input()))

# print(lans)
lans.sort()
start, end = 1, max(lans)
# print(start, end)

while start <= end:
    mid = (start+end)//2
    
    # lan 개수세기
    count = 0
    for item_lan in lans:
        count+= (item_lan//mid)
        
    # print('count: ', count)
    if count >= necess_lan:
        start = mid + 1
        # print('count>= necess')
        flag = 0
    else:
        end = mid - 1
        # print('count < necess')
        flag = 1

# print(start, mid, end, flag)

if flag:
    print(start-1)
else:
    print(mid)