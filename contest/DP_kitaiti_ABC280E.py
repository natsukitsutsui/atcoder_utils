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

N, P = LMI()

def Division(a: int, b: int, m: int):
    return (a * pow(b, m-2, m)) % m

p = Division(P, 100, mod1)
p_ = Division(100-P, 100, mod1)

dp = [0]*(N+1)

dp[1] = 1

for i in range(2, N+1):
    dp[i] = ((dp[i-2]+1)*p + (dp[i-1]+1)*p_) % mod1

print(dp[N])