import numpy as np

# Criando um array em Numpy (vetor)
arr = np.array([1, 2, 3, 4, 5])
print("Array em Numpy:")
print(arr)

# Operações matemáticas em arrays
print("\n Array multiplicando por 2:")
print(arr * 2)

arr2 = np.array([10, 20, 30, 40, 50])
print("\nSoma entre dois arrays:")
print(arr + arr2)

# Criando uma matriz (2D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("\n Matriz 2x3:")
print(matriz)

# Soma e média da Matriz
print("\n Soma de todos os elementos da matriz:")
print(np.sum(matriz))

print("\n Média de todos os elementos da matriz:")
print(np.mean(matriz))

# Transposta da matriz
print("\n MAtriz Transposta:")
print(matriz.T)

# Gerando número aleatórios
print("\n Números aleatórios entre 0 e 1:")
print(np.random.rand(3, 3))
# Gera uma matriz de 3x3 com valores aleatórios entre 0 e 1