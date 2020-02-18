#   Tip String
"""
Em Python um dado é considerado String sempre que :

1) Estiver entre aspas simples --> 'uma string'
2) Estiver entre aspas duplas --> "uma string"
3) Estiver entre aspas simples triplas --> '''uma string'''
4) Estiver entre aspas duplas triplas 
"""

"""
nome = 'Geek university'
print (nome)
print(type(nome))

nome = "Geek university"
print (nome)
print(type(nome))

nome = '''Geek university'''
print (nome)
print(type(nome))

nome = "Gina's bar"
print (nome)
print(type(nome))

nome = 'Angelina \nJolie'
print (nome)
print(type(nome))
"""
nome='Geek University'
print(nome.upper())

print(nome.lower())

print(nome.split()) #   Transforma em uma lista de Strings

print (nome[0:4])   #   Slice de string

print(nome[5:15])   #   Slice de string

print(nome.split()[0])  #   pega a 1a ocorrencia da lista de string

print(nome.split()[1])  #   pega a 2a ocorrencia da lista de string

#   [::-1]  --> comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])   #   Inversão da String

print(nome.replace('G', 'P'))

nome='ana'  #   ana é um palindromo
print(nome)

print(nome[::-1])

