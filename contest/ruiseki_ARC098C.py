"""
ARC 098 C
累積和
https://atcoder.jp/contests/arc098/tasks/arc098_a

"""

def LI(): return list(map(int, input().split()))
def II(): return int(input())

N = II()
S = input()

# 向きを変える必要がある人数の最小値を保持する関数
min_turn = 300000

sum_W = [0]
for i in range(N):
    if S[i] == "W":
        sum_W.append(sum_W[i]+1)
    else:
        sum_W.append(sum_W[i])

for i in range(N):
    # リーダーiより西側にいて西を向いている人数
    w = sum_W[i]
    # リーダーiより東側にいて東を向いている人数
    e = (N-i-1) - (sum_W[N]-sum_W[i+1])

    # 人iをリーダーとしたときの向きを変える必要がある人数
    turn = w + e

    # 最小値の更新
    min_turn = min(min_turn, turn)

print(min_turn)