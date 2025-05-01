import datetime
print("=== MENÚ INTERACTIVO ===")
for _ in range(100):
    print("\nSeleccione una de las siguientes opciopnes: ")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")
    opcion = input("Opción (1-3): ")
    if opcion == "1":
        print("¡Hola! espero tengas un gran día")
    elif opcion == "2":
        print("La fecha es:", datetime.datetime.now().strftime("%d/%m/%Y"))
    elif opcion == "3":
        print("Saliendo. ¡Hasta la próxima!")
        break
    else:
        print("La opción no es válida. Por favor, elige 1, 2 o 3.")