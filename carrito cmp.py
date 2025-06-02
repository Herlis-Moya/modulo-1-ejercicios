
cesta = []

while True:
    print("\nMenú de la cesta de la compra")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar")

    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        item = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cesta.append((item, precio))
        print(f"{item} agregado a la cesta.")

    elif opcion == "2":
        if not cesta:
            print("La cesta está vacía.")
        else:
            print("\nContenido de la cesta:")
            for item, precio in cesta:
                print(f"- {item}: ${precio:.2f}")

    elif opcion == "3":
        item = input("Ingrese el nombre del producto a eliminar: ")
        nueva_cesta = []
        encontrado = False

        for nombre, precio in cesta:
            if nombre == item and not encontrado:
                encontrado = True
            else:
                nueva_cesta.append((nombre, precio))

        if encontrado:
            cesta = nueva_cesta
            print(f"{item} eliminado de la cesta.")
        else:
            print("El elemento no se encuentra en la cesta.")

    elif opcion == "4":
        total = sum(precio for _, precio in cesta)
        print(f"El total de la cesta es: ${total:.2f}")

    elif opcion == "5":
        print("Gracias por su compra")
        break

    else:
        print("Opción inválida. Por favor, intente de nuevo.")
