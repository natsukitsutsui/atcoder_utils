"""
典型アルゴリズム E 
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e
ワーシャルフロイド法
"""

def LI(): return list(map(int, input().split()))
def II(): return int(input())

N,M = LI()
 
INF = 10**18
 
#全ての距離を無限として置いておく
dist = [[INF]*N for _ in range(N)]

# グラフの辺を受け取り, distに書き込む
for _ in range(M):
    u,v,c = LI()
    dist[u][v] = c
 
#iからiへの距離は0
for i in range(N):
    dist[i][i] = 0
 
#ワーシャルフロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
 
# 全ての頂点の組について最短距離を計算する
ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)