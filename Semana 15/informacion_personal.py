# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Marlon Salan",
    "edad": 20,
    "ciudad": "Ambato",
    "profesion": "Contador"
}

# Guardar una copia del diccionario original antes de modificarlo
diccionario_original = informacion_personal.copy()

# Mostrar el diccionario original
print("Diccionario original:")
for clave, valor in diccionario_original.items():
    print(f"{clave}: {valor}")

# Acceder y modificar la clave "ciudad"
nueva_ciudad = input("\nIngrese el nuevo nombre de la ciudad para modificar: ")
informacion_personal["ciudad"] = nueva_ciudad

# Agregar una nueva clave-valor "profesion" (preguntamos al usuario)
nueva_profesion = input("Ingrese una nueva profesión para la persona: ")
informacion_personal["profesion"] = nueva_profesion

# Verificar si existe la clave "telefono", si no existe la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Mostrar el diccionario modificado (ya no tendrá 'edad')
print("\nDiccionario modificado:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
