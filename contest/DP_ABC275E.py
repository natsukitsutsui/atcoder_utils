"""
ABC 275 E
https://atcoder.jp/contests/abc275

DPの持ち方を工夫, 逆元の前計算によって計算量を抑える
dp[i][j]: i回ルーレットを回したときにjマス目にいる確率と定義

"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())


def Division(a: int, b: int, m: int):
    return (a * pow(b, m-2, m)) % m


N, M, K = LI()
mod = 998244353

# dp[i][j]: i回ルーレットを回したときにjマス目にいる確率
dp = [[0]*(N+1) for _ in range(K+1)]
# 0回目に0にいる確率は1
dp[0][0] = 1

# m^(-1)を前計算することで計算量を減らせる
# 今回の問題ではこうしないと計算時間overになる
m_inv = Division(1, M, mod)

# 配るDP
# K回ルーレットを回す
for i in range(K):
    # マスj
    for j in range(N):
        # ルーレットの出目
        for m in range(1, M+1):
            # dp[i][j]が0でない(到達したことがあるマス)
            if dp[i][j] != 0:
                # Nマスを超える場合戻る
                if j+m > N:
                    tmp = 2*N - (j+m)
                else:
                    tmp = j+m
                # 配るDP
                # 前計算しておくことで計算量はO(NMK + log(mod))となる
                dp[i+1][tmp] += dp[i][j] * m_inv % mod
                # これだと計算量オーバー(O(NMKlog(mod)))
                # dp[i+1][tmp] += Division(dp[i][j], M, mod)

ans = 0
for i in range(K+1):
    ans += dp[i][N]
    ans %= mod

print(ans)
