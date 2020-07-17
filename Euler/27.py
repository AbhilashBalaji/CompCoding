'''
n^2 + an + b  |a| < 1k,|b| <= 1k  
'''

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    # print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def quad(a,b,n):
    return is_prime(abs(n**2 + a*n + b))


max = 0
max_s = (0,0)
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0 
        while True:
            if quad(a,b,n):
                n+=1
            else :
                break
        if n>1:
            print(a,b,n)
        if n > max:

            max = n
            max_s = (a,b)
        n = 0

print(max,max_s)



