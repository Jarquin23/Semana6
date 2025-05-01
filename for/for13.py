#Suma de numeros impares
suma = 0
for contador in range(1, 101):
    if contador % 2 != 0:
        suma+= contador
print(f"La suma de los números impares del 1 al 100 es: {suma}")