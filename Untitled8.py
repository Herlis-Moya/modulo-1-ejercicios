precio = int(input("Coloca precio"))

descuento = 15 / precio * 100

total = precio - descuento

if precio > 100:
    print(total)
else:
    print(precio)
