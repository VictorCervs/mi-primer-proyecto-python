#INICIO - (Aquí irían las definiciones de tus 2 funciones)

def areaCuadrado (lado1):
    calcularAreaCuadrado = lado1 * lado1
    return calcularAreaCuadrado

def areaRectangulo (base,altura):
    calcularAreaRectangulo = base * altura
    return calcularAreaRectangulo

#// Empieza el programa principal
#MOSTRAR "Bienvenido a la Calculadora de Áreas"
#PEDIR al usuario la figura y GUARDARLA en 'eleccion'
#SI 'eleccion' es igual a "cuadrado" ENTONCES:
#// ¿Qué harías aquí adentro? (Pista: pedir el lado, usar try/except, llamar a la función del cuadrado, mostrar resultado)

print("Bienvenido a la calculadora de figuras")

    
eleccion = input("Por favor introduce el nombre de tu figura: ").lower()
if eleccion == "cuadrado":

    try:

        lado1Text = input("Por favor introduce la medida de 1 lado: ")
        lado1 = float(lado1Text)

        resultadoAreaCuadrado = areaCuadrado(lado1)
        print(f"El area de tu cuadrado es: {resultadoAreaCuadrado}")

    except ValueError:

            print("Por favor introduce un valor valido")


#SI NO, SI 'eleccion' es igual a "rectangulo" ENTONCES:
#// ¿Qué harías aquí adentro? (La misma lógica, pero para el rectángulo)

elif eleccion == "rectangulo":

    try: 

        baseText = input("Por favor introduce la medida de tu base: ")
        base = float(baseText)

        alturaText = input("Por favor introduce la medida de tu altura: ")
        altura = float(alturaText)

        resultadoAreaRectangulo = areaRectangulo (base,altura)
        print(f"El area de tu rectangulo es: {resultadoAreaRectangulo}")

    except ValueError:

        print("Por favor introduce un valor valido")

    
#SI NO (ELSE):
#// ¿Qué harías aquí? (Mostrar el error de 'opción no válida')

else:
    print("No valido")