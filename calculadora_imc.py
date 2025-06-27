#// --- Parte 1: Entradas ---
#MOSTRAR "Bienvenido a la Calculadora de Índice de Masa Corporal (IMC)"

print("Bienvenido a la Caluladora de Indice de Masa Corporal (ICM)")
  
#PEDIR al usuario su peso en kg y GUARDARLO en la variable 'peso'

peso_texto = input("Por favor introduce tu peso en KG: ")

#CONVERTIR 'peso' a un número con decimales (float)

peso_numero = float(peso_texto)
  
#PEDIR al usuario su altura en metros y GUARDARLO en la variable 'altura'

altura_texto = input("Por favor introduce tu altura en Metros: ")

#CONVERTIR 'altura' a un número con decimales (float)

altura_numero = float(altura_texto)

#// --- Parte 2: Cálculos y Lógica ---
#// Calculamos el IMC
#CALCULAR imc = peso / (altura * altura)

imc = peso_numero / (altura_numero * altura_numero)

#// Decidimos el diagnóstico. Usamos una variable para guardarlo.
#DECLARAR variable 'diagnostico' como texto vacío 

diagnostico = ""

#SI imc es menor que 18.5 ENTONCES
#asignar "Bajo peso" a la variable 'diagnostico'

if imc < 18.5:
    diagnostico = "Bajo peso"
  
#SI NO, SI imc es menor que 25 ENTONCES  // (No hace falta comprobar si es >= 18.5, ¡porque si no, ya habría entrado en el 'if' anterior!)
#asignar "Peso normal" a la variable 'diagnostico'

elif imc < 25:
    diagnostico = "Peso normal"
      
#SI NO, SI imc es menor que 30 ENTONCES // (Misma lógica, ya sabemos que es >= 25)
#asignar "Sobrepeso" a la variable 'diagnostico'

elif imc < 30:
    diagnostico = "Sobrepeso"
      
#SI NO (si no fue ninguno de los anteriores, por descarte es >= 30)
#asignar "Obesidad" a la variable 'diagnostico'

else:
    diagnostico = "Obesidad"

#// --- Parte 3: Salidas ---
#MOSTRAR "Calculando su resultado..."

print("Calulando su resultado...")

#MOSTRAR "Su IMC es: " + el valor de 'imc' (formateado a dos decimales)

print(f"Su IMC es: {imc:.1f}")

#MOSTRAR "Su diagnóstico es: " + el valor de 'diagnostico'

print(f"Su diagnóstico es: {diagnostico}")

#FIN