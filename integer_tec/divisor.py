def make_divisors(n: int):
    """
    約数列挙を行うプログラム
    ex.
    input:
        840
    output: 
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 20, 21, 24, 28, 30, 35, 40, 
        42, 56, 60, 70, 84, 105, 120, 140, 168, 210, 280, 420, 840]
    計算量:
        O(sqrt(N))
    """
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]