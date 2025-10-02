# Crear y escribir en el archivo my_notes.txt
# El modo "w" crea el archivo o sobrescribe si ya existe
with open("my_notes.txt", "w") as archivo:
    archivo.write("Nombre: Marlon Salan\n")      # Primera línea
    archivo.write("Edad: 20 años\n")             # Segunda línea
    archivo.write("Ciudad: Ambato\n")            # Tercera línea
print(" ")
print("El archivo 'my_notes.txt' ha sido creado con la información.")
