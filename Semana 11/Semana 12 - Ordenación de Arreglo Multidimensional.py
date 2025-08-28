# Ordenación de todas las filas en una matriz bidimensional

matriz = [
    [15, 9, 30],
    [50, 25, 10],
    [45, 60, 5]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_todas_filas(matriz):
    for fila in matriz:
        bubble_sort(fila)

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos las filas
ordenar_todas_filas(matriz)

print("\nMatriz después de ordenar todas las filas:")
for fila in matriz:
    print(fila)
