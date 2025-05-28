dia = input("Ingresa un día de la semana (en minúsculas): ")

if dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana!")
elif dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "jueves" or dia == "viernes":
    print("Es un día de semana.")
else:
    print("Por favor, ingresa un día válido.")
