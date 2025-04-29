#Hacer un programa que de la tabla de multiplicar a partir de un numero dado por el usuario
from for3 import mostrarNumeros
def tablaMultiplicar(numero=0):
    for i in range(1, 12):
        print(f"{numero} * {i} = {numero*i}")
def main():
    num = int(input("Ingrese un numero: "))
    tablaMultiplicar(num)
    mostrarNumeros(num, 10)
main()