import collections

def prime_factorize(n):
    """
    素因数分解を行うプログラム
    ex.
    input:
        840
    output:
        Counter({2: 3, 3: 1, 5: 1, 7: 1}) 辞書型
    計算量:
        O(sqrt(N))
    """
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

c = prime_factorize(840)
print(c)
print(c.values())
print(c.keys())