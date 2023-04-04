"""
pastbook オリジナル問題
SegmentTree
"""

from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys, math, itertools, pprint, fractions
sys.setrecursionlimit(10**8)
mod1 = 998244353
mod2 = 10**9+7
INF = 10**100
def LMI(): return list(map(int, input().split()))
def II(): return int(input())
def LI(): return list(input())
def IN(): return input()
def IS(): return input().split()


"""
Segment Tree
区間に対する処理が、次の条件を満たすO(1)の演算であるとき、セグメント木を使うことで
O(logn)で処理することが出来る

・ 結合法則 (a・b)・c = a・(b・c)
・ 単位元eが存在する
"""


class SegmentTree:
    def __init__(
        self,
        n,              # 列の長さ
        identity_e,     # 単位元
        combine_f,      # 2つのデータから値を合成させるための関数
    ):
        self._n = n
        self._size = 1
        while self._size < self._n:
            self._size <<= 1
        self._identity_e = identity_e
        self._combine_f = combine_f
        self._node = [self._identity_e]*(2*self._size)

    # 配列の各要素を登録する
    def build(self, array):
        assert len(array) == self._n
        for index, value in enumerate(array, start=self._size):
            self._node[index] = value
        for index in range(self._size - 1, 0, -1):
            self._node[index] = self._combine_f(
                self._node[index << 1 | 0],     # 左の子
                self._node[index << 1 | 1],     # 右の子
            )

    # [一点更新] 位置 index (0-indexed) を値 value で更新
    def update(self, index, value):
        i = self._size + index
        self._node[i] = value
        while i > 1:
            i >>= 1
            self._node[i] = self._combine_f(
                self._node[i << 1 | 0],     # 左の子
                self._node[i << 1 | 1],     # 右の子
            )

    # [区間取得] 位置 [l, r) (0-indexed) 内の要素について、
    # l 番目から順に combine_f を適用した結果を示す (交換法則が前提になくてもよい)
    def fold(self, L, R):
        L += self._size
        R += self._size
        value_L = self._identity_e
        value_R = self._identity_e
        while L < R:
            if L & 1:
                value_L = self._combine_f(value_L, self._node[L])
                L += 1
            if R & 1:
                R -= 1
                value_R = self._combine_f(self._node[R], value_R)
            L >>= 1
            R >>= 1
        return self._combine_f(value_L, value_R)


N, Q = LMI()
A = LMI()

segment_tree = SegmentTree(N, INF, min)
segment_tree.build(A)

for _ in range(Q):
    t, x, y = LMI()
    if t == 1:
        segment_tree.update(x, y)
    else:
        print(segment_tree.fold(x, y))
