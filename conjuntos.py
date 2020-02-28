"""
Conjuntos

-   Conjuntos em qualquer linguagem de programação estamos fazendo referencia a Teoria dos conjuntos
    da Matematica

-   Em Python os conjuntos são chamados de Sets
-   Sets não possuem valores duplicados.
-   Sets não possuem valores ordenados
-   Os elementos não são acessiveis via indice

Os conjuntos (Sets) são referenciados em Python com {}

Diferencas entre Conjuntos (Sets) e Mapas (dicionarios):
-   Um dicionario tem chave/valor
-   Um conjunto tem apenas valor

"""

s = set({1,2,3,4,5,5,6,7,2,3})  #   note que temos valores repetidos
print(s)
print(type(s))
#   Em um conjunto os valores repetidos serão ignorados

s1= {1,2,3,4,5,5}
print(s1)
print(type(s1))

if 3 in s1:
    print('Tem o 3')

lista = [99,2,34,23,2,12,1,44,5,34]
print(f'Lista: {lista}')

tupla = 99,2,34,23,2,12,1,44,5,34
print(f'Tupla: {tupla}')

dicionario = {}.fromkeys([99,2,34,23,2,12,1,44,5,34], 'dict')
print(f'Dicionario: {dicionario}')

conjunto = {99,2,34,23,2,12,1,44,5,34}
print (f'Conjunto: {conjunto}')
print('---------------------------------------------')

#   Adiconando elementos em um conjunto
s2={1,2,3}
s2.add(4)
s2.add(4) # duplicidade não gera erro
print(s2)
print('---------------------------------------------')

#   remover elemento
#   Neste caso se o valor não for encontrado da erro
ret = s2.remove(3)
print(s2)
print('---------------------------------------------')

#   nesse caso se o valor não for encontrado não gera erro.
s2.discard(2)
print(s2)