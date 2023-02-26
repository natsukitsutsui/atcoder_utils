"""
第一回アルゴリズム実技検定 I
https://atcoder.jp/contests/past201912-open/tasks/past201912_i

bitDP
集合をキーとして動的計画法を解く
"""

def LI(): return list(map(int, input().split()))
def II(): return int(input())

N,M = LI()

# 1始まりにするためダミーを入れる
S = [0]
C = [0]

for _ in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == "Y":
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

# 集合としてあり得るものの個数, 2**Nと同じ
ALL = 1<<N

# cost[i][n]: セットiまで見て揃った部品の集合がnであるときのコストの最小値
cost = []
INF = 10**100
for i in range(M+1):
    cost.append([INF]*ALL)

#初期条件
cost[0][0] = 0

# iが小さいものから順に計算
for i in range(1, M+1):
    for n in range(ALL):
        # セットiを買わない
        cost[i][n] = min(cost[i][n], cost[i-1][n])
        # セットiを買う
        cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])

ans = cost[M][ALL-1]
if ans == INF:
    ans = -1

print(ans)