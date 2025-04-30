#Promedio de calificaciones
suma = 0
contador = 0
for _ in range(1000):
    calificacion = float(input("Dime una calificación (o -1 para terminar): "))
    if calificacion == -1:
        break
    suma += calificacion
    contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las calificaciones es: {promedio}")
else:
    print("Las calificaciones ingresadas no son válidas.")