# SETS "CONJUNTOS"
# COLEÇÃO MUTALVEL 
# NAO GARANTE ORDEM 
# NÃO HA INDICE 

# CRIAR SETS VAZIOS 

dias = set()
dias.add('Segunda')
dias.add('terca')
print(dias)

# conjuntos inicializados

frutas = {'maça', 'uva', 'pera', 'laranja'}
print(frutas)
print(type(frutas))

# remover 
#frutas.remove('uva')
frutas.discard('uva')
print(frutas)

print(len(frutas))  

# converter lista para sets 
lista = [5, 7, 4, 1, 2, 8, 13, 6]
conjunto_set = set(lista)
print(conjunto_set)