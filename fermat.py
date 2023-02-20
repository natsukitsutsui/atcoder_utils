"""
フェルマーの小定理を利用した法mでの二項係数の高速計算を行うプログラム
memo: 
    フェルマーの小定理
    「pを素数, bをpの倍数でない任意の整数としたとき
        b^(p-1) ≡ 1 (mod p)
    が成立する」
    これを変形することで
        b^(p-2) ≡ b^(-1)
    が得られる.つまりbの逆元はb^(p-2)と等価である.
    そのため 
        a / b ≡ a * b^(p-2) (mod p)
    である.
    この結果を用いて二項係数の計算の高速化を行う.

前計算:
    1!~n!の計算を行う(計算結果はfact[i])
計算量:
    O(n)

ex.
input:
    ncr(20000, 10)
output:
    136920883
計算量:
    O(logM) (Mはmodの値)

"""

def Division(a: int, b: int, m: int):
    return (a * pow(b, m-2, m)) % m

def ncr(n: int, r: int):
    return Division(fact[n], fact[r] * fact[n-r] % mod, mod)

mod = 10**9+7
fact = [0, 1]
N = 20000
for i in range(2,N+1):
    fact.append(fact[i-1] * i % mod)

print(ncr(20000, 10))
