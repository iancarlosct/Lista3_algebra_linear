import numpy as np

def gram_schmidt(vetores):
    vetores = [np.array(v, dtype=float) for v in vetores]
    ortogonais = []

    for v in vetores:
        w = v.copy()
        for u in ortogonais:
            w -= np.dot(v, u) / np.dot(u, u) * u
        ortogonais.append(w)
    
    return ortogonais

vetores = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

resultado = gram_schmidt(vetores)
for i, v in enumerate(resultado):
    print(f"u{i+1} =", v)
