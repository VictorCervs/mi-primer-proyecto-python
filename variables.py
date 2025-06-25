#1 Variables para almacenar datos personales
mi_nombre = "Victor cervantes"
mi_edad = 23 # Edad real
mi_estatura_metros = 1.63 # Estatura real
es_estudiante = True

#2 Variables para información de un productor
nombre_producto = "Laptop Gaming x"
precio_producto= 1200.50
stock_disponible = 10
esta_en_oferta = False

#3 Imprime el valor de cada variable
print("---Información Personal (usando f-strings) ---")
print(f"Nombre: {mi_nombre}")
print(f"Edad: {mi_edad}")
print(f"Estatura (metros): {mi_estatura_metros}")
print(f"Es estudiante: {es_estudiante}")

print("\n--- Información del producto (usando f-strings) ---")
print(f"Nombre del Producto: {nombre_producto}")
print(f"Precio: {precio_producto}")
print(f"Stock: {stock_disponible}")
print(f"En Oferta: {esta_en_oferta}")

#4 Imprime el tipo de cada variable para verificar
print("\n--- Tipo de datos (Usando f-strings)---")
print(f"Tipo de mi_nombre: {type(mi_nombre)}")
print(f"Tipo de mi_edad: {type(mi_edad)}")
print(f"Tipo de mi_estatura_metros: {type(mi_estatura_metros)}")
print(f"Tipo de es_estudiante: {type(es_estudiante)}")
print(f"Tipo de nombre_producto: {type(nombre_producto)}")
print(f"Tipo de precio producto: {type(precio_producto)}")
print(f"Tipo de stock_disponible: {type(stock_disponible)}")
print(f"Tipo de esta_en_oferta: {type(esta_en_oferta)}")

