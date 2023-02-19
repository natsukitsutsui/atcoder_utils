import math

"""
mathライブラリのよく使う機能についてまとめ
"""

# x以上の最小の整数を出力
# O(1)
math.ceil(x)

# x以下の最大の整数を出力
# O(1)
math.floor(x)

# x!を出力
# O(x)
math.factorial(x)

# 最大公約数を出力
# O(log(x+y))
math.gcd(x, y)

# 最小公倍数を出力
# O(log(x+y))
math.lcm(x, y)

# xのy乗を出力(mを指定することでmod mの形で出力)
# O(log(y))
math.pow(x, y, m)

# x個の中からy個を選ぶ組み合わせの数を出力
math.comb(x, y)