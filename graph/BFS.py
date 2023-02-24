# 幅優先探索
# dequeをimport
from collections import deque

# 頂点数N, 辺情報E, 始点s
N = int(input())
E = []
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(False)
    E.append(row)
s = int(input())

# N個のFalseで初期化した配列visited
visited = []
for _ in range(N):
    visited.append(False)

# キューの用意
Q = deque()
# 始点を到達済みにする
Q.append(s)
visited[s] = True

# キューを取り出しながら探索
while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        if not visited[j]:
            visited[j] = True
            Q.append(j)
