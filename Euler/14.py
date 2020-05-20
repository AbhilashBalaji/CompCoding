# memoised
cnt = 0

collatzdict = {1: 1}


def collz(x):
    if x in collatzdict.keys():
        pass
    elif x % 2 == 0:
        collatzdict[x] = 1 + collz(int(x/2))

    else:
        collatzdict[x] = 1 + collz(int(3*x + 1))

    return collatzdict[x]

for i in range(1, 1000000):
    if i not in collatzdict.keys():
        collz(i)

print(max(collatzdict, key=collatzdict.get))
