"""
第二回 アルゴリズム実技検定 G
https://atcoder.jp/contests/past202004-open/tasks/past202004_g
クエリ(キューでデータを管理)
"""
from collections import deque
from string import ascii_lowercase


def LI(): return list(map(int, input().split()))
def II(): return int(input())


Q = II()
que = deque()

for _ in range(Q):
    value = input().split()
    if value[0] == "1":
        # クエリ1の処理
        c = value[1]
        x = int(value[2])
        que.append([c, x])
    else:
        # クエリ2の処理
        d = int(value[1])
        # 各アルファベットがいくつ消されたかを格納
        cnt = {}
        for c in ascii_lowercase:
            cnt[c] = 0

        # 合計d個取り出すか, キューが空になるまで続ける
        while d > 0 and len(que) > 0:
            c, x = que[0]
            if d >= x:
                # 全部取れるパターン
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                # 途中で切るパターン
                cnt[c] += d
                que[0][1] -= d
                d = 0
        # 答えを計算する
        ans = 0
        for c in ascii_lowercase:
            ans += cnt[c] ** 2
        print(ans)
