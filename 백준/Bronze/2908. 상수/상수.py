org = input().split()
non_org = []
for item in org:
    k = str(item[::-1])
    non_org.append(k)
if non_org[0] > non_org[1]:
    print(non_org[0])
else:
    print(non_org[1])