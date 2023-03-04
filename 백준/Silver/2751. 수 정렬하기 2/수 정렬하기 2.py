import sys
list_number = int(sys.stdin.readline())
number_list = []
for number in range(list_number):
    number_list.append(int(sys.stdin.readline()))
number_list.sort()
for item in number_list:
    print(item)