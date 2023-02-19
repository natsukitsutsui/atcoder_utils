import collections

# 素因数分解
def prime_factorize(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            fac.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        fac.append(n)
    fac = collections.Counter(fac)
    return fac

c = prime_factorize(67280421310722)
print(c)
print(c.values())
print(c.keys())