"""
第一回 アルゴリズム実技検定 J
https://atcoder.jp/contests/past201912-open/tasks/past201912_j
grid dijkstra
"""
import heapq


def LI(): return list(map(int, input().split()))
def II(): return int(input())


H, W = LI()
A = [LI() for _ in range(H)]


# ダイクストラ法で始点(si, sj)から各マスへの最短経路を求める
def grid_dijkstra(si, sj):
    dist = [[10**100]*W for _ in range(H)]
    que = []
    heapq.heapify(que)
    dist[si][sj] = 0
    que.append([0, si, sj])
    while len(que) > 0:
        d, i, j = heapq.heappop(que)
        if d > dist[i][j]:
            continue
        for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if 0 <= i2 < H and 0 <= j2 < W and d + A[i2][j2] < dist[i2][j2]:
                dist[i2][j2] = d + A[i2][j2]
                heapq.heappush(que, [dist[i2][j2], i2, j2])
    return dist


# 左下隅, 右下隅, 右上隅からの距離を求める
dist1 = grid_dijkstra(H-1, 0)
dist2 = grid_dijkstra(H-1, W-1)
dist3 = grid_dijkstra(0, W-1)

# T字路の交差点を全探索する
ans = 10**100
for i in range(H):
    for j in range(W):
        res = dist1[i][j] + dist2[i][j] + dist3[i][j] - 2*A[i][j]
        ans = min(ans, res)

print(ans)
