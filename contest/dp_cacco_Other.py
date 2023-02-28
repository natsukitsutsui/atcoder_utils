"""
第二回 アルゴリズム実技検定 K
https://atcoder.jp/contests/past202004-open/tasks/past202004_k
dp
"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())


N = II()

S = " " + input()
C = [0] + LI()
D = [0] + LI()

INF = 10**100

# dp[i][j]: i文字目までの扱いを決めて,
# そこまでの累積和がjであるときのコストの最小値
dp = [[INF]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(i):
        if S[i] == "(":
            # そのまま使う
            dp[i][j+1] = min(dp[i][j+1], dp[i-1][j])
            # 反転させる
            if j > 0:
                dp[i][j-1] = min(dp[i][j-1], dp[i-1][j]+C[i])
        else:
            if S[i] == ")":
                # そのまま使う
                if j > 0:
                    dp[i][j-1] = min(dp[i][j-1], dp[i-1][j])
                # 反転させる
                dp[i][j+1] = min(dp[i][j+1], dp[i-1][j]+C[i])
        # 削除する
        dp[i][j] = min(dp[i][j], dp[i-1][j]+D[i])

print(dp[N][0])
