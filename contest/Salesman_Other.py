"""
典型アルゴリズム C
巡回セールスマン問題
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())


N = II()
A = [LI() for _ in range(N)]

ALL = 1 << N
# cost[n][i]: 訪れた都市の集合がnで, 最後にいる都市がiであるときのコスト最小値
cost = [[10**100]*N for _ in range(ALL)]

# 初期条件.最初にいるときの始点はnに含めない
cost[0][0] = 0


# nで表現される集合に要素iが含まれるかどうかを判定してTrue/Falseを返す
def has_bit(n, i):
    return (n & (1<<i) > 0)


for n in range(ALL):
    for i in range(N):
        # iからjに移動する遷移をためす
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(cost[n | (1 << j)][j],
                                        cost[n][i]+A[i][j])

# 全都市を訪問して始点に戻ってくる最小のコスト
print(cost[ALL-1][0])
