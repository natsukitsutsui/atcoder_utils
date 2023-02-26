def LI(): return list(map(int, input().split()))
def II(): return int(input())

N, X, Y = LI()
A = LI()

base = 10**4
import math

# x軸方向のdp
# dpx[i][j]: i回目の移動でjの位置にたどり着けるか
# index0　が -10^4, index10^4 が 0
dpx = [[False]*(2*10**4+1) for _ in range(math.ceil(N/2))]
dpy = [[False]*(2*10**4+1) for _ in range(math.floor(N/2))]

dpx[0][base+A[0]] = True
dpy[0][base] = True
i = 1
j = 0
while i+j < N:
    if i > j:
        for y in range(2*10**4+1):
            if dpy[j][y]:
                dpy[j+1][y+A[i+j]] = True
                dpy[j+1][y-A[i+j]] = True
        j += 1
    else:
        for x in range(2*10**4+1):
            if dpx[i][x]:
                dpx[i+1][x+A[i+j]] = True
                dpx[i+1][x+A[i+j]] = True
        i += 1

if dpx[-1][X] and dpy[-1][Y]:
    print("Yes")
else:
    print("No")

