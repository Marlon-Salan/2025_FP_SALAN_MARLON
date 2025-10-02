# Abrir el archivo en modo lectura
archivo = open("my_notes.txt", "r")

print(" ")
print("Contenido del archivo:\n")

# Leer cada línea con readline()
linea = archivo.readline()
while linea:  # Mientras haya texto en la línea
    print(linea.strip())  # strip() elimina saltos de línea innecesarios
    linea = archivo.readline()

# Cerrar el archivo
archivo.close()
