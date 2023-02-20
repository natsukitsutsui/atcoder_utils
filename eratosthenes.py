def eratosthenes(n):
    """
    エラトステネスの篩
    n以下の素数の列挙を行うプログラム
    input:
        12
    output:
        (各indexが素数であればTrue,そうでなければFalse)
        [False, False, True, True, False, True, False,
         True, False, False, False, True, False]
    計算量:
        O(NlogN)
    """
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime