def f(L, n=42000):
    d = [0]*n
    for i in xrange(1, n):
        for j in xrange(i, n, i):
            d[j] += 1
        c = d[i-1] * d[i//2] if i % 2 == 0 else d[(i-1)//2] * d[i]
        if c > L:
            return c, i*(i-1)//2


L = int(input("First triangular number to exceed this many divisors:"))
Dt, t = f(L)
print "is", t, "(", Dt, "divisors)"
