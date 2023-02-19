from bisect import bisect_left, bisect_right

# ソート済みのリストaに対して,xを挿入できる位置を返す.
# aにxが含まれる場合,右に入れるか左に入れるかはleft,rightで選択できる.
# left -> 指定値以下
# right -> 指定値超過

a = [1, 2, 2, 2, 3, 5]

print(bisect_left(a, 2))  # -> 1
print(bisect_right(a, 2))  # -> 4