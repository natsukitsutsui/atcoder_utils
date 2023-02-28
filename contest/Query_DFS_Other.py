"""
第一回 アルゴリズム実技検定 K
https://atcoder.jp/contests/past201912-open/tasks/past201912_k?lang=ja
クエリ(DFS)
独立したクエリを別々に求めるのではなく, 木を探索しながら一気に全てを求めるという方針
"""

import sys
sys.setrecursionlimit(10**7)


def LI(): return list(map(int, input().split()))
def II(): return int(input())


N = II()
# 根(社長の頂点番号)
R = -1

# edges[i]: 頂点iの子(部下)の頂点番号たち
edges = [[] for _ in range(N)]
for i in range(N):
    p = II()
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

# クエリを受け取り,aの値で分類する
# queries[i]: aの値に対応する. [クエリ番号, bの値]を並べた配列
queries = [[] for _ in range(N)]
Q = II()
for q in range(Q):
    a, b = LI()
    queries[a-1].append([q, b-1])

# 答えとなる配列
ans = [False]*Q
# boss[i]: 頂点iが今見ている頂点の上司ならTrue
boss = [False]*N


# 再帰関数で深さ優先探索を実装する
def dfs(i):
    # クエリを処理
    for q, b in queries[i]:
        ans[q] = boss[b]
    # 自分自身を上司に設定する
    boss[i] = True
    # 再帰的に子を見ていく
    for j in edges[i]:
        dfs(j)
    # 抜けるときに自身を上司から外す
    boss[i] = False


# 根に対して呼び出す
dfs(R)

# 答えをまとめて出力する
for q in range(Q):
    if ans[q]:
        print("Yes")
    else:
        print("No")
