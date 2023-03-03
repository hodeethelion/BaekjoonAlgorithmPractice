for _ in range(int(input())):
    a = input().split()
    rep = int(a[0])
    letter = a[1]
    temp = ''
    for let in letter:
        for i in range(rep):
            temp = temp+ let
    print(temp)
            
            