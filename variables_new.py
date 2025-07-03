#DEFINIR la función "calcular" que acepta numero1, numero2, y operacion.

def calcular(num1,num2,operacion):

#SI la operacion es "sumar":
#DEVOLVER la suma de numero1 y numero2.
    operacion = operacion.lower()

    if operacion == "sumar":
        return num1 + num2 

#SINO SI la operacion es "restar":
#DEVOLVER la resta de numero1 y numero2.

    elif operacion == "restar":
        return num1 - num2 

#SINO SI la operacion es "multiplicar":
#DEVOLVER el producto de numero1 y numero2.

    elif operacion == "multiplicar":
        return num1 * num2 

#SINO SI la operacion es "dividir":
#// Dentro de la división, comprobar si el divisor es cero.
#SI numero2 es igual a 0:
#DEVOLVER el mensaje de error "Error: No se puede dividir por cero".
#SINO:
#DEVOLVER la división de numero1 entre numero2.

    elif operacion == "dividir":
        if num2 == 0:
            return "Error: No se puede dividir por 0"
        
        else:
            return num1 / num2

#// Si ninguna de las condiciones anteriores fue verdadera, la operación no es válida.
#SINO:
#DEVOLVER el mensaje de error "Operación no válida".
#FIN DE LA FUNCIÓN.

    else:
        return "Operación no válida"

#----- Interfaz ----------
print ("Bienvenido a la calculadora mágica")

num1_texto = input("Por favor ingresa tu primer número: ")
num2_texto = input("Por favor ingresa tu segundo número ")
operacion = input("Por favor elige la operación a realizar (sumar, restar, multiplicar, dividir)")

try: 
    num1 = float(num1_texto)
    num2 = float(num2_texto)

    resultado_final = calcular(num1,num2,operacion)

    print(f"El resultado es: {resultado_final}")

except ValueError:
    print("Error: Por favor introduce números validos")
