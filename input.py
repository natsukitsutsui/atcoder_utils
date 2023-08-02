from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys, math, itertools, pprint, fractions
from decimal import Decimal
sys.setrecursionlimit(10**8)
mod1 = 998244353
mod2 = 10**9+7
INF = math.inf
def II(): return int(input())
def LI(): return list(input())
def IN(): return input()
def IS(): return input().split()
def LMI(): return list(map(int, IS()))
def Vertical_IN(n): return zip(*[LMI() for _ in range(n)])
def Build_Graph(n, m):
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = LMI()
        a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)
    return G
def array_copy(A, n, m=0, l=0):
    if m == 0: return [A[i] for i in range(n)]
    elif l == 0: return [A[i][:] for i in range(n)]
    else: return [[A[i][j][:] for j in range(m)] for i in range(n)]
