import sys
input = sys.stdin.readline
total_sugar = int(input())
# 5킬로 3개 3킬로

bag = 0

def get_bag(sugar):
    global bag
    while sugar>= 0:
        if sugar % 5 == 0 :
            bag += (sugar // 5)
            print(bag)
            break
        sugar -=3
        bag += 1
    else:
        print(-1)
get_bag(total_sugar)