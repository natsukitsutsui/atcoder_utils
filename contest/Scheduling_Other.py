"""
典型アルゴリズム問題集 B
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b
貪欲法
"""
def LI(): return list(map(int, input().split()))
def II(): return int(input())

N = II()
# 終了日でソートするために[終了日, 開始日]の順に格納する
BA = []
for i in range(N):
    a, b = LI()
    BA.append([b, a])
BA.sort()

ans = 0
last = 0
for b, a in BA:
    if last < a:
        ans += 1
        last = b

print(ans)