#número de digitos
num = float(input("Ingrese un numero positivo: "))
while num <= 0:
    num = int(input("Por favor, introduce un numero positivo: "))
cont_digitos = 0
for digito in str(num):
    cont_digitos += 1
print(f"El numero tiene {cont_digitos} dígitos.")