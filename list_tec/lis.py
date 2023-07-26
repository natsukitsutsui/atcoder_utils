"""
LIS
最長増加部分列の計算

n: 要素数
seq: 計算するリスト

与えられたリストにおける最長増加部分列の要素数を数える
返り値の LIS は最長増加部分列そのものでないことに注意する

計算量: O(NlogN)
"""
def lis(n, seq):
    LIS = [seq[0]]
    for i in range(n):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect_left(LIS, seq[i])] = seq[i]
    return len(LIS), LIS
