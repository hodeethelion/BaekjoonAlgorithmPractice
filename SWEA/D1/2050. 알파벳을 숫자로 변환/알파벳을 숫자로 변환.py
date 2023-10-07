alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test_case = input().rstrip()
for case in test_case:
    print(alphabet.index(case)+1, end=' ')