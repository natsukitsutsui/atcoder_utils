"""
ARC 017 C
半分全列挙
https://atcoder.jp/contests/arc017/tasks/arc017_3

要素を半分ずつのグループに分けて,それぞれのグループについて
部分集合の全列挙を行い、その結果を組み合わせることで答えを求める.

要素数Nとしては30~40が目安
"""

def LI(): return list(map(int, input().split()))
def II(): return int(input())

from collections import defaultdict

N, X = LI()

# 偶数番目と奇数番目で半分に振り分けていく
A = []
B = []
for i in range(N):
    w = II()
    if i%2==0:
        A.append(w)
    else:
        B.append(w)

# nで表現される集合に要素iが含まれるかどうかを判定して
# True/Falseを返す
def has_bit(n, i):
    return (n & (1<<i) > 0)

# グループBを全列挙して重さ合計ごとに集計
dic = defaultdict(int)
for n in range(1<<len(B)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += B[i]
    dic[s] += 1

# グループAを全列挙して答えを求める
ans = 0
for n in range(1<<len(A)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += A[i]
    ans += dic[X-s]

print(ans)
