"""
ABC 276 C
https://atcoder.jp/contests/abc276/tasks/abc276_e
深さ優先探索
"""
import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
C = []
for _ in range(H):
    row = list(input())
    C.append(row)

for h in range(H):
    for w in range(W):
        if C[h][w] == "S":
            sx, sy = h, w


def dfs(x, y, d):
    if y >= W or y < 0 or x >= H or x < 0 or C[x][y] == "#":
        return

    if d == 0 and C[x][y] == "S":
        pass
    elif d < 4 and C[x][y] == "S":
        return
    elif C[x][y] == "S":
        print("Yes")
        exit()
    else:
        C[x][y] = "#"

    dfs(x+1, y, d+1)
    dfs(x-1, y, d+1)
    dfs(x, y+1, d+1)
    dfs(x, y-1, d+1)


dfs(sx, sy, 0)
print('No')