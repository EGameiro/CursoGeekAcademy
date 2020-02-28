"""
Mapas -> Conhecidos em Python como Dicionários


"""
receita = {'jan':100, 'fev':250, 'mar':400}
print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

#   Desempacotamento de Dicionario
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')