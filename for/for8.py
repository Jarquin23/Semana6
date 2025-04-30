#Adivinar un numero
import random
num_sec = random.randint(1, 10)
for intento in range(1, 11):
    intento_usuario = int(input("Adivina el numero entre 1 y 10: "))
    if intento_usuario == num_sec:
        print("¡Felicitaciones! Adivinaste el número")
        break
    elif intento_usuario < num_sec:
        print("Intenta con un numero mayor a este.")
    else:
        print("Intenta con un numero menor a este.")