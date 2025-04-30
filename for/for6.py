#Suma de numeros hasta alcanzar un límite
suma = 0

for _ in range(1000):
    numero = int(input("Introduce un número: "))
    suma += numero
    if suma > 100:
        break

print("La suma total es:", suma)
