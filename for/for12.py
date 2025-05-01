#Serie de Fibonacci
n = int(input("¿Cuántos números de la serie Fibonacci deseas generar?"))
a, b = 0, 1
print("Serie de Fibonacci:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b