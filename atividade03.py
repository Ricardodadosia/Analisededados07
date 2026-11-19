numeros = []

for i in range(12):
    numero = int(input(f"digite o {i+1} numero inteiro: " ))
    numeros.append(numero)

numeros.sort()

print("\nNumeros em ordem crescente:")
print(numeros)