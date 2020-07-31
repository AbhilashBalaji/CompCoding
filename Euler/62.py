from itertools import permutations


def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x

def cntPerm(n):
    # blacklist = []
    cnt = 0
    perms = [int(''.join(p)) for p in permutations(str(n))]
    for i in perms :
        if i not in blacklist and is_perfect_cube(i):
            cnt+=1
            # print(i)
            # print(i)
            blacklist.append(i)
            
    # print(perms)
    return cnt

blacklist = []
i = 345

while True :
    cube = i ** 3
    if  cube not in blacklist and cntPerm(cube)>4:
        print(cube)
        # print(blacklist)
        break
    i+=1
