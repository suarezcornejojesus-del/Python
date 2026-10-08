# 1. Lectura de datos por teclado
precio = float(input("Introduce el precio unitario del producto (€): "))
unidades = int(input("Introduce la cantidad de unidades: "))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento (%): "))

# Constantes del programa
PORCENTAJE_IVA = 21  # 21% de IVA
UMBRAL_ENVIO_GRATUITO = 100.0  # Umbral en euros para envío gratis

# 2. Cálculos usando operadores aritméticos y asignaciones
subtotal = precio * unidades[cite: 1]
descuento = subtotal * (porcentaje_descuento / 100)[cite: 1]
subtotal_con_descuento = subtotal - descuento[cite: 1]

importe_iva = subtotal_con_descuento * (PORCENTAJE_IVA / 100)[cite: 1]
total = subtotal_con_descuento + importe_iva[cite: 1]

# 3. Expresión condicional (operador ternario) para el envío gratuito
envio_gratis = "Sí" if total >= UMBRAL_ENVIO_GRATUITO else "No"[cite: 1]

# 4. Muestra de resultados con formateo a 2 decimales (:.2f)
print("\n--- RESUMEN DE LA FACTURA ---")
print(f"Subtotal: {subtotal:.2f} €")[cite: 1]
print(f"Descuento ({porcentaje_descuento}%): -{descuento:.2f} €")[cite: 1]
print(f"IVA ({PORCENTAJE_IVA}%):          +{importe_iva:.2f} €")[cite: 1]
print(f"Total:             {total:.2f} €")[cite: 1]
print(f"¿Envío gratuito?:  {envio_gratis}")