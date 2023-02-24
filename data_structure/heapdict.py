"""
HeapDict

heapqとdictを合わせたデータ構造

計算量:
    要素の挿入: O(logn)
    要素の削除: O(logn)
    要素の存在確認: O(1)
    最小値の取得:O(1)
使い方:
    # HeapDictを定義
    hd = HeapDict()

    # xを挿入
    hd.insert(x)

    # xを削除
    hd.erase(x)

    # xの存在確認
    if hd.is_exist(x):

    # 最小値の取得
    x = hd.get_min()

"""
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