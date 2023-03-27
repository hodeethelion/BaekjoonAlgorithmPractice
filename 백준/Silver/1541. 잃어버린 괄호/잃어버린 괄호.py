#식의 값을 최소로 만들려고 한다 
import sys
input = sys.stdin.readline
string = str(input().strip())
# print(string)
# print(string.split('-'))
divided_list = string.split('-')
ans = 0
for number, item in enumerate(divided_list):
    # print(number, item)
    template = 0
    for sub_item in item.split('+'):
        template += int(sub_item)
    
    if number == 0:
        ans += template
    if number >= 1:
        ans -= template
print(ans)
