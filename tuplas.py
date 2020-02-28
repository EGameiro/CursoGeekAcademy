"""
Tuplas

Tuplas são bastante parecidas com Listas
Exintem duas diferenças :

1- As tuplas são representadas por ()
2- As tuplas são imutáveis. Isso significa que depois de criada ela não muda. 
   Toda operação em uma Tupla gera uma nova Tupla.

"""

tupla1 = (1,2,3,4,5,6)
print(tupla1)

#   Isso tambem é entendido como uma tupla
tupla2 = 1,2,3,4,5,6,7
print(tupla2)

#   Tupla com um elemento não é uma tupla é um INT
tupla3=(4)
print (tupla3)

#   Podemos gerar uma tupla dinamicamente com range
tupla4 = tuple(range(11))
print (tupla4)
print('-------------------------------------------------')

#   As opções de SUM, MAX, MIN e LEN também funcionam nas Tuplas

#   Verificar se um determinado elemento está contido na Tupla
tupla5=(1,2,3)
print(3 in tupla5)
print('-------------------------------------------------')

#   Devemos utilizar Tuplas sempre que não for necessario alterar a coleção
#   Exemplo : ('Janeiro', 'Fevereiro'.......)

