import math

ans = set()



def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    return list(set(divs))

for i in range(1,10000):
    a = sum(divisors(i))
    print(a,i)
    if sum(divisors(a)) == i:
        # print(a,i)
        ans.add(a)
        ans.add(i)


print(sum(ans))

