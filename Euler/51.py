def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        # print('\t',f)
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def repeatingDigits(num):
    digits = {}
    num_s = str(num)
    for i in range(len(num_s)):
        digit = num_s[i]
        if digit not in digits.keys():
            digits[digit] = []
        digits[digit].append(i)
    return digits


def genPossible(num,digits, key):
    num_s = str(num)
    ans = []
    for i in range(1,10):
        num_s2=num_s.replace(key,str(i))
        num_2 = int(num_s2)
        if is_prime(num_2):
            ans.append(num_2)

    return ans

n = 100
blacklist = []
while True:
    n += 1
    flag = 0
    if not is_prime(n) or n in blacklist:
        continue
    digits = repeatingDigits(n)
    for i in digits.keys():
        if len(digits[i]) > 1:
            primes = genPossible(n,digits,i)
            blacklist += primes
            if len(primes) >7:
                print(n)
                flag =1 
                print(primes)
                break 
    if flag == 1 :
        break
