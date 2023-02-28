"""
第三回 アルゴリズム実技検定 M
https://atcoder.jp/contests/past202005-open/tasks/past202005_m
BFS + Salesman
"""
from collections import deque


def LI(): return list(map(int, input().split()))
def II(): return int(input())


N, M = LI()

# 隣接リスト
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = LI()
    G[u-1].append(v-1)
    G[v-1].append(u-1)

S = II()-1
K = II()
T = LI()
T = [T[i]-1 for i in range(K)]

# 実装上, T[K] = Sとしておく
T.append(S)

# Dist[k][l]: 頂点T[k]からT[l]までのコスト
Dist = []
for t1 in T:
    # 幅優先探索
    INF = 10**100
    dist = [INF]*N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        i = que.popleft()
        for j in G[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                que.append(j)
    # 巡回セールスマン問題に帰着させたときに使いやすくしておく
    res = [dist[t2] for t2 in T]
    Dist.append(res)

# 巡回セールスマン問題
# cost[n][i]: Tの中で訪れた集合がnで,
# 最後にいる頂点がT[i]であるときのコストの最小値
ALL = 1 << K
cost = [[INF]*K for _ in range(ALL)]

# 始点Sから各T[i]に移動した状態を初期状態とする
for i in range(K):
    cost[1 << i][i] = Dist[K][i]


# nで表現される集合に要素iが含まれるか判定
def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(K):
        # iからjに移動する遷移を試す
        for j in range(K):
            # すでに訪問済みか, 同じ頂点は無視する
            if has_bit(n, j) or i == j:
                continue
            # 事前計算したT[i]からT[j]への最短距離を使う
            cost[n | (1 << j)][j] = min(cost[n | (1 << j)][j],
                                        cost[n][i] + Dist[i][j])

# K個の頂点を全て訪問して, どこかの頂点にいる中での最小のコスト
print(min(cost[ALL-1]))
