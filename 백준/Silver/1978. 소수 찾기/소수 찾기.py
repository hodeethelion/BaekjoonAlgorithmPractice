k = input()
numbers = list(map(int, input().split()))
num_sosu = 0

for num in numbers:
    if num == 1:
        continue
    error = 0
    for i in range(2,num):
        #소수가 아닐때
        if num % i == 0:
            error +=1
    if error == 0:
        num_sosu+= 1
    # print(num, error)
print(num_sosu)