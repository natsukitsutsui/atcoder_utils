""""
ABC 278F bitDP
https://atcoder.jp/contests/abc278/tasks/abc278_f
"""


from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys, math, itertools, pprint, fractions
sys.setrecursionlimit(10**8)
mod1 = 998244353
mod2 = 10**9+7
INF = 10**100
def LMI(): return list(map(int, input().split()))
def II(): return int(input())
def LI(): return list(input())
def IN(): return input()
def IS(): return input().split()

N = II()
S = []
for i in range(N):
    s = IN()
    first = ord(s[0]) - ord("a")
    last = ord(s[-1]) - ord("a")
    S.append([first, last])

ALL = 2**N

dp = [0]*ALL
def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(N):
        if has_bit(n, i):
            dp[n] |= (((1<<S[i][0]) & ~dp[n^(1<<i)]) >> S[i][0]) << S[i][1]

print("First" if dp[ALL-1] else "Second")
