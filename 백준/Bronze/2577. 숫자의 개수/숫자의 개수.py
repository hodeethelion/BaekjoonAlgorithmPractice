a = int(input())
b = int(input())
c = int(input())
string_k = str(a*b*c)
for i in range(10):
    print( string_k.count(str(i)))