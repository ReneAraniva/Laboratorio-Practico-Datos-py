matriz = [
 [5, 8, 2],
 [1, 6, 9],
 [4, 7, 3]
]
print("Matriz original:")
print(matriz)
print("----"*20)

#calcule la suma de la diagonal principal
suma_diagonal = sum(matriz[i][i] for i in range(len(matriz)))
print(f"Suma de la diagonal principal: {suma_diagonal}")
print("----"*20)

#Calcule la suma de la diagonal inversa
suma_diagonal_inversa = sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))#Suma diagonal inversa con for
print(f"Suma de la diagonal inversa: {suma_diagonal_inversa}")
print("----"*20)

#Encuentre el número mayor y menor de la matriz.
num_mayor = max(max(fila) for fila in matriz)#Número mayor de la matriz
print(f"Número mayor de la matriz: {num_mayor}")

num_menor = min(min(fila) for fila in matriz)#Número menor de la matriz
print(f"Número menor de la matriz: {num_menor}")
