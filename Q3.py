def gauss_jordan(A, b):
    n = len(A)

    for i in range(n):
        A[i] = A[i] + [b[i]]

    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("Pivô zero — sistema pode não ter solução única.")

        for j in range(i, n + 1):
            A[i][j] /= pivot

        for k in range(n):
            if k != i:
                fator = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= fator * A[i][j]

    x = [A[i][-1] for i in range(n)]
    return x

A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b = [8, -11, -3]

solucao = gauss_jordan(A, b)
print("Vetor solução x:", solucao)
