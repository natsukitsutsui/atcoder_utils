"""
第一回 アルゴリズム実技検定 L
https://atcoder.jp/contests/past201912-open/tasks/past201912_l
プリム法
小さい制約に注目して全探索をかける
"""
import heapq
import math


def LI(): return list(map(int, input().split()))
def II(): return int(input())


N, M = LI()

# 大きい塔のxyc
xyc_large = [LI() for _ in range(N)]
# 小さい塔のxyc
xyc_small = [LI() for _ in range(M)]


def has_bit(n, i):
    return (n & (1 << i) > 0)


# [x1, y1, c1]と[x2, y2, c2]を結ぶ塔のコスト計算
def calc_edge_cost(xyc1, xyc2):
    x1, y1, c1 = xyc1
    x2, y2, c2 = xyc2
    cost = math.hypot(x1-x2, y1-y2)
    if c1 != c2:
        cost *= 10
    return cost


ans = 10.0**100

# 小さい塔の中で使うものの集合を全探索
for b in range(1 << M):
    xyc_use = []
    # 大きい塔は全部使う
    for xyc in xyc_large:
        xyc_use.append(xyc)
    for i in range(M):
        if has_bit(b, i):
            xyc_use.append(xyc_small[i])
    sz = len(xyc_use)

    # プリム法で最小全域木を求める
    que = []
    heapq.heapify(que)
    used = [False]*sz
    que.append([0.0, 0])
    res = 0.0

    while len(que):
        cost, i = heapq.heappop(que)
        if not used[i]:
            res += cost
            used[i] = True
            for j in range(sz):
                if not used[j]:
                    cost = calc_edge_cost(xyc_use[i], xyc_use[j])
                    heapq.heappush(que, [cost, j])
    ans = min(ans, res)

print(ans)
