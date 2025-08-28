# Búsqueda en una matriz bidimensional

matriz = [
    [10, 25, 30],
    [40, 55, 60],
    [70, 85, 90]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, (-1, -1)


# Buscar
valor_buscado = 90
encontrado, posicion = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if encontrado:
    print(f"\n El valor {valor_buscado} fue encontrado en la posición {posicion}.")
else:
    print(f"\n El valor {valor_buscado} no se encuentra en la matriz.")
