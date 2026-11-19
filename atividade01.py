vendas = []

for i in range(10):
    venda = float(input(f'informe o valor da venda: '))
    vendas.append(venda)

total = sum(vendas)   
print(f'\nVendas completadas: {vendas} ')
print(f'\nTotal das vendas {total :2f}')
