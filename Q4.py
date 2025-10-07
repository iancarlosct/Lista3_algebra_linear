import numpy as np

def base_dimensao(vetores):
    A = np.array(vetores, dtype=float)

    posto = np.linalg.matrix_rank(A)

    Q, R = np.linalg.qr(A.T) 
    base = []
    for i in range(R.shape[1]):
        if np.abs(R[i, i]) > 1e-10:
            base.append(A[i])
    
    return base, posto

vetores = [
    [1, 1, 0],
    [2, 2, 0],
    [0, 1, 1]
]

base, dimensao = base_dimensao(vetores)
print("Base:", base)
print("Dimensão:", dimensao)
