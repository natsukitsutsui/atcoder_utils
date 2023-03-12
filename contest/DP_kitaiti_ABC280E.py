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


H, W = LMI()
G = [LI() for _ in range(H)]
visited = [[False]*W for _ in range(H)]
visited[0][0] = True

sx, sy = 0, 0
while True:
    if G[sx][sy] == 'from collections import Counter, defaultdict, deque
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


N, M, T = LMI()
A = [0] + LMI()
X = []
Y = []
for _ in range(M):
    x,y = LMI()
    X.append(x)
    Y.append(y)

x_i = 0
for i in range(1, N):
    if x_i < M and i == X[x_i]:
        T += Y[x_i]
        x_i += 1
    
    if T > A[i]:
        T -= A[i]
    else:
        print("No")
        exit()

print("Yes")'