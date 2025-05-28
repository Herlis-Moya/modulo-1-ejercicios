usuario_correcto = "admin"
contraseña_correcta = 1234

usuario = input("Introduce nombre de usuario.")
contraseña = int(input("Introduce la contraseña"))
if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido. Bienvenido!")
else:
    print("Acceso denegado. Usuario o contraseña incorrectos.")