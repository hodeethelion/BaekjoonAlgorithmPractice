n = int(input())
number_list =[]
for _ in range(n):
    number_list.append(int(input()))
number_list = sorted(number_list)
for i in number_list:
    print(i)