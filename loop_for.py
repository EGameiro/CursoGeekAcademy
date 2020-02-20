"""
Loop For
Loop => Estrutura de repetição
For => Uma dessas estruturas
"""

nome='Geek University'
lista=[1, 3, 5, 7, 9]
numeros=range(1, 10)    # Temos que transformar em uma lista

"""
for letra in nome:  #Iterando em uma String
    print(letra)

for numero in lista:    #Iternado sobre lista
    print(numero)

for numero in range(1, 10):
    print(numero)

Obs : O enumerate traz sempre uma dupla que é o indice e o valor
    EX : enumerate de NOME ==> ((0, 'G', 1, 'e', 2, 'e', 3,'k'..........))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[1])

for valor in enumerate(nome):
    print(valor[0])

qtde=int(input('Quantas vezes esse loop deve rodar..?'))
for n in range(1, qtde+1):
    print(f'Imprimindo {n}')

"""
for letra in nome:
    print(letra, end='') # imprime cada um dos caracteres sem pular de linha

