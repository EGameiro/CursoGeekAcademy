"""
Dicionários


"""
#   Forma mais comum
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py':'Paraguay'}
print(paises)

#   Acessando elementos
print(paises['br'])
print(paises['eua'])

pais = paises.get('py')
print(pais)