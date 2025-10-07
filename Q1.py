def matriz_transposta(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposta = matriz_transposta(matriz)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)
