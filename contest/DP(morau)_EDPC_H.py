"""
EDPC H
https://atcoder.jp/contests/dp/tasks/dp_h
貰うDP
"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())


H, W = LI()
A = [list(input()) for _ in range(H)]

mod = 10**9+7

# dp[i][j]: i行j列での経路数
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1


for i in range(H):
    for j in range(W):
        # 壁ならカウントしない
        if A[i][j] == "#":
            continue
        # 左と上から遷移する
        if i > 0:
            dp[i][j] += dp[i-1][j] % mod
        if j > 0:
            dp[i][j] += dp[i][j-1] % mod

print(dp[H-1][W-1] % mod)
