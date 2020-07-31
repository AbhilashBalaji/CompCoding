# https://wikimedia.org/api/rest_v1/media/math/render/svg/bb6b6388ded7d1e160a3bd82b60c5b593947088a
result = 1 


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



def gen(n):
    primes = []
    for i in range(2,201):
        if is_prime(i):
            primes.append(i )
    return primes

primes  = gen(1)
i = 0
limit = 1000000
while result * primes[i] < limit :
    result *= primes[i]
    i+=1

print(result)
