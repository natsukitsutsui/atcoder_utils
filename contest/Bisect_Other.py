"""
第三回 アルゴリズム実技検定 J
https://atcoder.jp/contests/past202005-open/tasks/past202005_j?lang=ja
二部探索
"""
import bisect


def LI(): return list(map(int, input().split()))
def II(): return int(input())


N, M = LI()
A = LI()

# B[k]: 子供kが食べた寿司の美味しさ最大値の-1倍
# bisectは広義単調増加の配列しか扱えないため
B = [0]*N

for a in A:
    # 寿司を食べる子供を二部探索で探す
    k = bisect.bisect_right(B, -a)
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a