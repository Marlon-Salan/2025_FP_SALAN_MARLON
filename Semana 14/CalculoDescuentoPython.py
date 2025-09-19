def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar en base al monto total y porcentaje.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
print("=== Sistema de Compras con Descuento ===")

# Primera interacción (usa 10% por defecto)
print("\n--- Primera Compra ---")
monto1 = float(input("Ingrese el valor total de la primera compra: "))
descuento1 = calcular_descuento(monto1)
print(f"Monto total de la compra: ${monto1:.2f}")
print(f"Descuento (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto1 - descuento1:.2f}")

# Segunda interacción (el usuario elige el porcentaje)
print("\n--- Segunda Compra ---")
monto2 = float(input("Ingrese el valor total de la segunda compra: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
descuento2 = calcular_descuento(monto2, porcentaje)
print(f"Monto total de la compra: ${monto2:.2f}")
print(f"Descuento ({porcentaje}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto2 - descuento2:.2f}")
