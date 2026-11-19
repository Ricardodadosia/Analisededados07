numeros = []
resposta = 'S'

while resposta == 'S':
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)  

   
    resposta = input("Deseja continuar? [S/N]: ").strip().upper()

quantidade = len(numeros)  

print(f'\nValores computados: {numeros}')
print(f'Quantidade de números: {quantidade}')
