import itertools

"""
itertoolsの使い方
参考: https://qiita.com/anmint/items/37ca0ded5e1d360b51f3

"""
# 累積和
# 累積和をリストで出力
ary = [1, 3, 5, 7, 9]
cumsum = itertools.accumulate(ary)
print(list(cumsum))
# -> [1, 4, 9, 16, 25]
# 文字列でも使える
s = ['ab', 'bc', 'cd']
print(list(itertools.accumulate(s)))
# -> ['ab', 'abbc', 'abbccd']

# groupby
# リストの最初から数えて同じ値のものを区切って出力
bi = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = itertools.groupby(bi)
for key, group in gr:
    print(f'{key}: {list(group)}')
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]

# 順列
# 指定したリストの要素の順列の全パターンを出力, 第二引数に何個取り出すか(nPrのr)を指定できる
print(list(itertools.permutations([1, 2, 3])))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 組み合わせ
# 指定したリストの要素の組み合わせを出力
print(list(itertools.combinations([1, 2, 3], 2)))
# -> [(1, 2), (1, 3), (2, 3)]

# 直積
print(list(itertools.product([0,1], repeat=3)))
# -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]


