"""
正方行列の足し, 引き, 積の演算
"""
class Matrix:
    def __init__(self, N, A):
        self.n = N
        self.A = A
    
    def __add__(self, other):
        return [[self.A[i][j] + other.A[i][j]\
                  for j in range(self.n)] for i in range(self.n)]
    
    def __sub__(self, other):
        return [[self.A[i][j] - other.A[i][j]\
                  for j in range(self.n)] for i in range(self.n)]
    
    def __mul__(self, other):
        return [[sum([self.A[i][k] * other.A[k][j] for k in range(self.n)])\
                  for j in range(self.n)] for i in range(self.n)]
