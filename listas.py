"""
Listas em Python

As listas em Python são definidas por colchetes: []
"""

lista1 = [1,99,4,27,15,3,1,44,42,27]

lista2 = ['G', 'e', 'e','k','','U','n','i']

lista3=[]

lista4 = list(range(11))

lista5 = list('Geek University')

#   checar se determinado valor está na lista. Isso se aplica para qualquer tipo de Lista
num=18
if  num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'*** Não exnontrei o numero {num}')
    
#   Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

#   Podemos contar o numero de ocorrencias de um valor em uma Lista
#   Conta o numero de '1'
print(lista1.count(1))
#   Conta o numero de 'e'
print(lista5.count('e'))

#   Podemos adicionar elementos em um Lista usando a função APPEND
lista1.append(12)
#   lista1.append(12,14,16)  ==> isso não pode, da erro
print(lista1)

#   Com a função EXTEND pode-se adicionar mais que um elemento na lista
lista1.extend([123,232,434])
print(lista1)

#   Podemos inserir um novo elemento na LIsta informando a posição do indice
lista1.insert(2,'novo')
print(lista1)

#   Podemos juntar duas listas
lista1 = lista1 + lista2
print(lista1)

#   Podemos imprimir a Lista inversa
lista2.reverse()
print(lista2)

#   Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#   Contar os elementos de uma Lista
print(len(lista1))

#   Podemos remover o ultimo elemento de uma LIsta
lista5.pop()
print(lista5)

#   Podemos remover um elemento pelo indice.
lista5.pop(2)
print(lista5)

#   Podemos remover todos os elementos
lista5.clear

#   Podemos converter uma string para uma lista
#   Exmeplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#   exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#   Convertendo uma Lista em String
#   O comando abaixo diz para : Pegar a lista6, colocar um espaço entre cada elemento e transforma em uma strig
lista6 = ['Programação', 'em', 'Python', 'Essencial']
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)
print('----------------------------------------------------')

#   Podemos colocar qualquer tipo de dado em uma Lista, inclusive de tipos diferentes
lista7  =[1, 2.23, True, 'Geek', [1,2,3], 45698745]
print (lista7)
print('----------------------------------------------------')

#   Iterando sobre Listas
soma=0
for elemento in lista4:
    print(elemento)
    soma=soma + elemento
print(soma)
print('----------------------------------------------------')

carrinho=[]
produto = ''
produto='sair'  # comentar essa linha para executar o while abaixo
while produto != 'sair':
    print('Adicione um produto, tecle "sair" para parar')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#   Gerar indice em um FOR
cores = ['verde', 'amarelo', 'azul','branco']
for indice, cor in enumerate(cores):
    print(indice,cor)

#   Encontrar o indice de um elemento na lista
#   Caso o elemento não exista vai dar erro
#   Se houve elementos em duplicidade ele retorna o indice do 1o.
numeros=[5,6,7,8,9,10]
print(numeros.index(9))

#   Soma, Valor minimo, Valor Maximo, Tamanho
lista8 = [1,2,3,4,5,6]
print(sum(lista8))
print(max(lista8))
print(min(lista8))
print(len(lista8))

#   Transformando Lista em Tupla
lista9 = [1,2,3,4,5,6]
print(lista9)
print(type(lista9))

tupla = tuple(lista9)
print(tupla)
print(type(tupla))

