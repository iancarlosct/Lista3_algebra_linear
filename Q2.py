def determinante(m):
    n = len(m)

    if n == 1:
        return m[0][0]

    if n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    det = 0
    for j in range(n): 
        menor = [linha[:j] + linha[j+1:] for linha in m[1:]]
        cofator = ((-1) ** j) * m[0][j] * determinante(menor)
        det += cofator
    return det

matriz1 = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

matriz2 = [
    [2, -3, 1],
    [2, 0, -1],
    [1, 4, 5]
]

print("Determinante da matriz 1:", determinante(matriz1))  #22
print("Determinante da matriz 2:", determinante(matriz2))  #49
