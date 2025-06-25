#1 Saludo Inicial
print("Bienvenido al clasificador de películas por edad")

#2 Pedir la edad al usuario y guardarla como texto
edad_texto = input("Por favor, introduce tu edad: ")

#3 Convertir el texto a un número entero
edad_numero = int(edad_texto)

#4 Iniciar el bloque de decisiones
if edad_numero >=18:
    #Este bloque solo se ejecuta si la edad es de 18 o más
    print("Puedes ver todas las películas.")
    

elif edad_numero >= 13:
    #Este bloque solo se ejecuta si la edad NO es >= 18, PERO SÍ es >=13
    print("Puedes ver películas con clasifiación G y PG-13")

else:
    #Este bloque se ejecuta si nunguna de las condiciones anterior fue verdadera
    print("Puedes ver películas con clasificación G (Todos los públicos).")

#5 Mensaje final, se ejecuta simpre
print("¡Disfruta de la función!")
