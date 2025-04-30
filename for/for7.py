#contador regresivo
num = int(input("Dime un número positivo: "))
while num < 0:
    num = int(input("El numero debe ser positivo, intente de nuevo: "))
for i in range(num, -1, -1):
    print(i)