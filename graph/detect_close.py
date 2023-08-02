
"""
無向グラフの閉路検出

N頂点N本の辺
閉路が一つに限られる場合のみ使える
グラフをコピーして次数1の頂点を削除していくことで閉路を検出する。

連結グラフに閉路が2つ含まれる場合などには使えない
dfs で次数が奇数のものについて考えれば複数の閉路を含んでいても出来そう
"""

N = II()
G = [set() for _ in range(N)]
for _ in range(N):
    a, b = LMI()
    a -= 1; b -= 1
    G[a].add(b)
    G[b].add(a)

G_ = [G[i]|set() for i in range(N)]

Q = deque()
for i in range(N):
    if len(G_[i]) == 1:
        Q.append(i)

while Q:
    i = Q.popleft()
    if len(G_[i]) == 1:
        j = G_[i].pop()
        Q.append(j)
        G_[j].remove(i)

print(G_)
