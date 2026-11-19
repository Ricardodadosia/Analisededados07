produtos = []

for i in range(5):
    produto = input('informe o nome do produto: ')
    produtos.append(produto)

    print(produtos)  

    # Acesso ao elemento 
    n = int(input('digite o posicão do elemento a acessar: '))  
    print(produtos[n-1])

    # Alterando uma lista "nome de um elemento"
    produtos[n-1] = input(f'informe o nome do outro elemento na posição {n}: ')
    print(produtos)
