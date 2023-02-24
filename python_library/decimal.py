# 正確な四捨五入を行うためのライブラリ
# roundでは正確な結果が得られない

from decimal import Decimal, ROUND_HALF_UP
A, B = 7, 3
print(Decimal(str(B/A)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
# 0.429