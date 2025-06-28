# INICIO

# --- Parte 1: Configuración Inicial (Zona Segura) ---
# DEFINIR variable 'saldo' con el valor 1000.00
# PEDIR al usuario su nombre y GUARDARLO en 'nombre_usuario'
# MOSTRAR "Bienvenido " + nombre_usuario + " a VIC BANK."

saldo = 1000.00

nombre_usuario = input("Por favor introduce tu nombre: ")
print(f"Bienvenido {nombre_usuario} a VIC BANK")

# --- Parte 2: El Bloque de Transacción (Zona de Peligro) ---
# INTENTAR:
    # -- Todo el Plan A (el camino feliz) va aquí adentro, indentado --
    
    # MOSTRAR "Tu saldo actual es: $" + el valor de 'saldo'
    # PEDIR al usuario la cantidad a retirar y GUARDARLA en 'cantidad_texto'
    # CONVERTIR 'cantidad_texto' a número y GUARDARLO en 'cantidad_numero'

print(f"Tu saldo actual es: ${saldo:.2f}")

    # --- Inicio de las validaciones lógicas (en orden de eficiencia) ---
    # SI 'cantidad_numero' es menor o igual a 0 ENTONCES:
        # MOSTRAR "Error: La cantidad a retirar debe ser un número positivo."

    # SI NO, SI 'cantidad_numero' es mayor que 'saldo' ENTONCES:
        # MOSTRAR "Error: Fondos insuficientes. Tu saldo es de $" + el valor de 'saldo'
        
    # SI NO (esto es el "camino feliz", si pasó las dos validaciones anteriores):
        # Realizar la transacción
        # CALCULAR nuevo_saldo = saldo - cantidad_numero
        # Actualizar el saldo original para futuras transacciones (importante)
        # ASIGNAR el valor de 'nuevo_saldo' a 'saldo'
        # MOSTRAR "Retiro exitoso. Tu nuevo saldo es: $" + el valor de 'saldo'

try:

    cantidad_texto = input("Introduce la cantidad a retirar: ")
    cantidad_numero = float(cantidad_texto)

    if cantidad_numero <= 0:
        print("Error: la cantidad a retirar debe ser un número positivo")

    elif cantidad_numero > saldo:
        print(f"Error: fondos insuficientes. Tu saldo es de: $ {saldo:.2f}")

    else: 
        nuevo_saldo = saldo - cantidad_numero
        saldo = nuevo_saldo
        print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo:.2f}")

# --- Parte 3: Redes de Seguridad ---
# EXCEPTO si ocurre un ErrorDeValor (el usuario escribió texto):
    # MOSTRAR "Error: Por favor, introduce una cantidad numérica válida."

# EXCEPTO si ocurre un ErrorDeDivisionPorCero (el usuario escribió 0 como denominador):
    # (Nota: En este ejercicio no hay división, así que este except no es necesario,
    # pero lo dejamos aquí como recordatorio de la lección anterior. El único que necesitamos es ValueError).

except ValueError:
    print("Error: Por favor, introduce una cantidad númerica valida")

# FIN