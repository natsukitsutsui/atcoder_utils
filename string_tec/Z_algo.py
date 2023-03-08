def z_algo(S):
    """
    Zアルゴリズム
    計算量: O(N)
    
    長さNの文字列Sについて, 0以上|S|未満の全てのiに対してSとS[i:]の
    最大共通接頭辞の長さを求める

    ex.
    input: aaabaaaab
    output: [9, 2, 1, 0, 3, 4, 2, 1, 0]
    """
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        print(A)
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        print(A)
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A
