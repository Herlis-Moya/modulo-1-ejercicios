

opcion = input("\nEstas en un parque y encuentras una puerta oculta ¿Qué eliges? (ENTRAR/INFORMAR):\n").strip().upper()

if opcion == "ENTRAR":
    print("\nEntras  y encuentras animales enfermos en jaulas. ¿Quieres LLAMAR a la policia o REGRESAR e irte?")
    
    opcion = input("¿Qué haces? (LLAMAR/REGRESAR): ").strip().upper()
    
    if opcion == "LLAMAR":
        print("\nLlega la policia y se llevan a los animales a un centro medico y refugio. ¡Felicidades! Has hecho algo bueno.")

    elif opcion == "REGRESAR":
        print("\nDecides regresar e ignorar a los animales .Pero al regresar, te ven y te matan para que no hables")

    else:
        print("\nNo haces nada. Te quedas mirando, te encuentran y te matan")

elif opcion == "INFORMAR":
    print("\nDecides informar, pero te das cuenta que los del parque tienen una reccion molesta y se van hablar a otro lugar'. ¿Que harias ESCUCHAR a escondidas o IGNORAR e irte a casa?")
    
    opcion = input("¿Qué haces? (ESCUCHAR/IGNORAR): ").strip().upper()
    
    if opcion == "ESCUCHAR":
        print("\nAl escuchar a escondidas, descubres que tienen animales enfermos encerrados. Al querer irte te descubren  y te matan.")

    elif opcion == "IGNORAR":
        print("\nIgnoras su comportamiento y te vas a casa.")
    

else:
    print("\nTe quedas sin hacer nada. Sospechan y te matan.")