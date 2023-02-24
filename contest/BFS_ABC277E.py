"""
ABC 277 E
https://atcoder.jp/contests/abc277/tasks/abc277_e

状態のBFS
現在の状態の定義を適切に行って, 状態をBFSする
状態の数が実行時間内に収まるかの確認は必要
今回の場合,
    頂点の数(N) * スイッチのON, OFF(2)
のため十分収まることが分かる

"""
from collections import deque


def LI(): return list(map(int, input().split()))
def II(): return int(input())


N, M, K = LI()
G = [[] for _ in range(N)]

for _ in range(M):
    u, v, a = LI()
    u -= 1
    v -= 1
    G[u].append([v, a])
    G[v].append([u, a])

S = LI()
S = set([S[i]-1 for i in range(len(S))])

Q = deque()
# (現在の頂点, スイッチのON,OFF)
Q.append([0, 1])

visited = [[-1, -1] for _ in range(N)]
visited[0][1] = 0

# BFS
while len(Q) > 0:
    i, switch = Q.popleft()
    for j, a in G[i]:
        if i in S:
            if visited[j][a] == -1:
                visited[j][a] = visited[i][switch] + 1
                Q.append([j, a])
        else:
            if switch == a and visited[j][a] == -1:
                visited[j][a] = visited[i][switch] + 1
                Q.append([j, a])

# 出力
if visited[N-1][0] != -1 and visited[N-1][1] != -1:
    print(min(visited[N-1]))
elif visited[N-1][0] != -1:
    print(visited[N-1][0])
elif visited[N-1][1] != -1:
    print(visited[N-1][1])
else:
    print(-1)
