def LI(): return list(map(int, input().split()))
def II(): return int(input())
 
import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()
        self.size=0

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1
        self.size+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1
            self.size-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]
 
N, M, K = LI()
A = LI()
L_descend=HeapDict()
R_ascend=HeapDict()
 
Ans=[0]
for idx, v in enumerate(sorted(A[:M])):
    if idx < K:
        Ans[-1]+=v
        L_descend.insert(-v)
    else:
        R_ascend.insert(v)

# print(L_descend.d)
# print(R_ascend.d)

for l in range(N-M):
    r = l + M
    ans = Ans[-1]
    # print(A[l])
    # print(A[r])
    if L_descend.is_exist(-A[l]):
        L_descend.erase(-A[l])
        ans -= A[l]

        if R_ascend.size == 0 or R_ascend.get_min() > A[r]:
            L_descend.insert(-A[r])
            ans += A[r]
        else:
            min_R = R_ascend.get_min()
            R_ascend.erase(min_R)
            L_descend.insert(-min_R)
            ans += min_R
            R_ascend.insert(A[r])

    else:
        R_ascend.erase(A[l])
        if L_descend.get_min() > -A[r]:
            R_ascend.insert(A[r])
        else:
            min_L = -L_descend.get_min()
            L_descend.erase(-min_L)
            ans -= min_L
            R_ascend.insert(min_L)
            L_descend.insert(-A[r])
            ans += A[r]
    
    # print("L", L_descend.d)
    # print("R", R_ascend.d)

    Ans.append(ans)

print(" ".join(map(str, Ans)))