produtos = []

for i in range(2):
    produto = input('informe o nome do produto: ')
    produtos.append(produto)

    print(produtos)  

    # Acesso ao elemento 
    n = int(input('digite o posicão do elemento a acessar: '))  
    print(produtos[n-1])

    # Alterando uma lista "nome de um elemento"
    produtos[n-1] = input(f'informe o nome do outro elemento na posição {n}: ')
    print(produtos)


    # Removendo a lista 
    produto_a_remover = input('\nDigite o nome do produto a remover: ')
    if  produto_a_remover in produtos:
        produtos.remove(produto_a_remover)
    print(produtos)

    # Pesquisar os metodos insert, pop(), clear 