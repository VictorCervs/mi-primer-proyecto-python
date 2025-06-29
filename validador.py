def validador_password (password):
    if len(password) <8:
        return "Error la constaseña es demasiado corta"

    else:
        return True 

password_del_usuario = input("Por favor introduce tu contraseña: ")

resultado_validacion = validador_password(password_del_usuario)

print(f"{resultado_validacion}")



