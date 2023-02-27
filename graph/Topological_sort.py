import sys
sys.setrecursionlimit(10**6)

def topological_sort(G: list):
    """
    トポロジカルソートを行う関数
    閉路のあるグラフではトポロジカルソートをすることはできない
    G: 有向非巡回グラフ(DAG)
    return: 各ノードを始点としたときの経路の最大長
    """
    # ノードの数
    node = len(G)
    # 入次数. 始点の判定に行う
    indeg = [0]*node

    for i in range(node):
        for j in range(len(G[i])):
            indeg[G[i][j]] += 1
    
    # 頂点iから始まるパスの最大長
    length = [0]*node

    # lengthが既に計算済みかどうかを判定
    done = [False]*node

    def rec(i):
        # 計算済みであればすぐに値を返す
        if done[i]:
            return length[i]
        # そうでなければ値を計算する
        length[i] = 0
        for j in G[i]:
            length[i] = max(length[i], rec(j)+1)

        # 計算済みのフラグを立てる
        done[i] = True
        return length[i]
    
    # 全ての始点についてrecを呼び出す
    for i in range(node):
        if indeg[i] == 0:
            rec(i)
    
    return length



