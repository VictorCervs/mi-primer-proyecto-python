#INICIO
#MOSTRAR "Bienvenido a la Calculadora Robusta."

print("Bienvenido a la calculadora robusta.")

#// Aquí empieza nuestra "zona de peligro", así que ponemos la red de seguridad.
#INTENTAR:
#// -- Todo el Plan A (el camino feliz) va aquí adentro, indentado --

try: 
      
#PEDIR al usuario el numerador y GUARDARLO en 'numerador_texto'.

    numerador_texto = input("Por favor introduce tu primer valor")

#CONVERTIR 'numerador_texto' a número y GUARDARLO en 'numerador_num'.

    numerador_numero = float(numerador_texto)

#PEDIR al usuario el denominador y GUARDARLO en 'denominador_texto'.

    denominador_texto = input("por favor introduce tu segundo valor")

#CONVERTIR 'denominador_texto' a número y GUARDARLO en 'denominador_num'.

    denominador_numero = float(denominador_texto)

#// Ahora viene la segunda acción peligrosa: la división
#CALCULAR resultado = numerador_num / denominador_num

    resultado = numerador_numero / denominador_numero

#// Si llegamos hasta aquí, todo salió bien, así que mostramos el resultado
#MOSTRAR con f-string "El resultado de la división es: " + el valor de 'resultado'.

    print(f"El resultado de la división es: {resultado:.2f}")

#// Ahora vienen los Planes B (las redes de seguridad)

except ValueError: 

#EXCEPTO si ocurre un ErrorDeValor (el usuario escribió texto):
#MOSTRAR "Error: Por favor, introduce solo números válidos."

    print("Por favor introduce un valor numerico")

#EXCEPTO si ocurre un ErrorDeDivisionPorCero (el usuario escribió 0 como denominador):
#MOSTRAR "Error: No se puede dividir entre cero."

except ZeroDivisionError:

    print("Error no se puede dividir entre cero")

#FIN 