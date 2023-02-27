"""
典型アルゴリズム D
ダイクストラ法
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
"""

def LI(): return list(map(int, input().split()))
def II(): return int(input())

import heapq

N, M = LI()

# 隣接リスト
G = [[] for _ in range(N)]
for _ in range(M):
    u,v,c = LI()
    G[u].append([v, c])

def dijkstra(G: list, N: int):
    # 頂点0から各頂点への最短距離を保持する配列
    # N個の-1で満たしておく
    dist = [-1]*N

    # ダイクストラで使うヒープ
    Q = []
    
    # 始点となる頂点0をヒープに追加しておく
    # (距離, 頂点)として追加する
    heapq.heappush(Q, (0, 0))

    # 始点となる頂点0への最短経路は0となる
    dist[0] = 0

    # ヒープから取り出したことがあるかを保存する配列
    # 最初はN個のFalseで埋めておく
    done = [False]*N

    # ダイクストラ法で各頂点への最短経路を求める
    while len(Q) > 0:

        # ヒープの先頭の頂点を取り出してiとする
        d, i = heapq.heappop(Q)

        # もし前にヒープから取り出したことがあれば
        # 隣接する頂点を調べるのをスキップする
        if done[i]:
            continue

        # ヒープから頂点iを取り出したことを記録しておく
        done[i] = True

        # 頂点iに隣接する頂点を順番に見る
        # 見ている頂点をjとする
        # また,iからjへ移動するときに使う辺の重みをcとする
        for (j, c) in G[i]:

            # jが未訪問だったとき, あるいはjへの最短経路が更新可能だったとき
            # jへの最短経路を更新して, ヒープの末尾に追加する
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(Q, (dist[j], j))
    
    return dist
dist = dijkstra(G, N)
print(dist[N-1])

