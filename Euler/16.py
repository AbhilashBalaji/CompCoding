#lmaoo
def sumOfDigits(x):
    sum = 0
    for i in str(x):
        # print(i)
        sum+=int(i)
    return sum

print(sumOfDigits(2**1000))