"""
Unionfind

使い方:
    # UnionFindを定義
    uf = UnionFind(N)

    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    uf.parents

    # 要素xが属するグループの根を返す
    uf.find(x)

    # 要素xが属するグループと要素yが属するグループとを併合する 
    uf.union(x, y)

    # 要素xが属するグループのサイズ（要素数）を返す
    uf.size(x)

    # 要素x, yが同じグループに属するかどうかを返す
    uf.same(x, y)

    # 要素xが属するグループに属する要素をリストで返す
    uf.members(x)

    # すべての根の要素をリストで返す
    uf.roots()

    # グループの数を返す
    uf.group_count()

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    uf.all_group_members()

    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    print(uf)
"""

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
