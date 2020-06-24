from functools import reduce
num = 100


def fact(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


# print(fact(nm))
sum = 0
num_str = fact(num)
num_str = str(num_str)
for i in num_str:
    sum += int(i)
    print(i)
# print()

print(sum)
