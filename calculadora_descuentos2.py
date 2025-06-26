# calculadora_descuentos.py
# Creado por Víctor Cervantes con la guía de AlexDev

# 1. Bienvenida y obtención de datos
print("Bienvenido a la calculadora de descuentos.")
total_compra_texto = input("Por favor, ingrese el monto total de la compra: ")

# 2. Conversión de datos y manejo de errores (El desafío adicional que te propongo ahora)
try:
    total_compra_numero = float(total_compra_texto)
except ValueError:
    print("Error: Por favor, ingrese solo números.")
    exit() # Termina el programa si la entrada no es válida

# 3. Lógica de negocio y cálculos
monto_descuento = 0.0 # Inicializamos la variable

if total_compra_numero > 1000:
    # Regla 1: 15% de descuento
    monto_descuento = total_compra_numero * 0.15
elif total_compra_numero >= 500:
    # Regla 2: 10% de descuento
    monto_descuento = total_compra_numero * 0.10
# Si no, monto_descuento se queda en 0.0, que es lo correcto.

# Cálculo final
precio_final = total_compra_numero - monto_descuento

# 4. Presentación de resultados al usuario
print("--- Recibo ---")
print(f"Monto original:       $ {total_compra_numero:.2f}")
print(f"Descuento aplicado:   - $ {monto_descuento:.2f}")
print("--------------------")
print(f"Total a pagar:        $ {precio_final:.2f}")