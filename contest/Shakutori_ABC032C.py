"""
ABC 032 C
尺取り法
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


N, K = LMI()
S = [II() for _ in range(N)]

if 0 in S:
    print(N)
    exit()

l, r = 0, 0
prod = 1
ans = 0

for l in range(N):
    while r < N and prod * S[r] <= K:
        prod *= S[r]
        r += 1
    ans = max(ans, r-l)
    if r - l > 0:
        prod //= S[l]
    else:
        r += 1

print(ans)
