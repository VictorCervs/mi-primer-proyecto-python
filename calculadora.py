# Calculadora.py

print("---Calculadora Simple---")

# 1.- Solicitar al usuario el primer número (input devuelve string es necesario convertir)
num1_str = input("Introduce el primer número")
num1 = float(num1_str) # Se usa el float para permitir decimales

#2.- Solicitar al usuario el segundo número
num2_str = input("Introduce el segundo número")
num2 = float(num2_str) #Se usa float para permitir decimales

#3.- Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 #Considerar caso de división por 0

#4.- Imprimir los resultados usando f-strings
print("n\---- Resultados ---")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multipliación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

#5.- Demostrar un operador de asignación
resultado_acumulado = num1
resultado_acumulado += num2 #Equivalente a resultado_acumulado = resultado acumulado + num2
print(f"\nResultado acumulado (num1 += num2): {resultado_acumulado}")

#6.- Demostrar operadores de comparación y lógicos
print("\n--- Comparaciones ---")
print(f"{num1} es mayor que {num2}: {num1 > num2}")
print(f"{num1}. es igual a {num2}: {num1 == num2}")
print(f"Ambos números son positivas: {(num1 > 0) and (num2 > 0)}")
print(f"Alguno de los números es cero: {(num1 == 0) or (num2 == 0)}")
