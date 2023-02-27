"""
典型アルゴリズム F
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f
プリム法
"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())

import heapq
 
N, M = LI()

# 隣接リスト
G = [[] for _ in range(N)]
 
# 無効具ラグの重みを保存
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append([v, c])
    G[v].append([u, c])

# プリム法で最小全域木問題を解く
def prim(G: list, N: int):

    # 頂点がマークされているかどうかを管理する配列
    marked = [False]*N

    # マークされている頂点の数を保存する変数
    marked_count = 0

    # 最初に頂点0を選んでマークする
    marked[0] = True
    marked_count += 1

    # 次に選ぶ辺の候補を入れるヒープ
    Q = []

    # 頂点0に隣接する辺を調べ, ヒープに入れる
    for j, c in G[0]:
        heapq.heappush(Q, (c, j))
    
    # 最小全域木の重みの合計を保存する変数
    sum = 0
    
    # 全ての頂点がマークされるまで繰り返す
    while marked_count < N:

        # ヒープから最小の重みの辺を取り出す
        # (辺の重み, 選んだときにマークする頂点)
        c, i = heapq.heappop(Q)
    
        # 辺につながる頂点iもすでにマークされていた場合操作をスキップ
        if marked[i]:
            continue
        
        # 頂点iをマーク
        marked[i] = True
        marked_count += 1

        # 使った辺は最小全域木となるため, 重みを保存しておく
        sum += c
    
        # 新たにマークした頂点iに隣接する辺を調べる
        for (j, c) in G[i]:

            # 辺がつなぐ頂点がすでにマークされている場合はヒープに入れない
            if marked[j]:
                continue
    
            heapq.heappush(Q, (c, j))
    return sum

sum = prim(G, N)

print(sum)