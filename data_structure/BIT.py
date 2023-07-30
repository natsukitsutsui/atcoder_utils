"""
Binary Indexed Tree

N 個の変数: v1, ..., vn

クエリ
1. vi に値 w を加える
2. v1 + ... + va を求める

計算量
O(logN)

参考
http://hos.ac/slides/20140319_bit.pdf
"""

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
