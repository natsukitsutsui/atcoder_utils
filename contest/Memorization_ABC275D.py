"""
ABC 275 D
メモ化再帰

一度計算した結果をメモ(記憶)しておくことで、同じ引数を得た時に計算結果を再利用する
"""

from functools import lru_cache


@lru_cache(maxsize=1000)
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(int(input())))
