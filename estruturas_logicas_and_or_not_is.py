"""
Estruturas Logicas : AND , OR , NOT , IS

"""

ativo=False
logado=False

if ativo and logado:
    print("Bem vindo Usuario")
else:
    print("Você precisa ativar sua conta")

if not ativo:
    print("Você precisa ativr sua conta")
else:
    print("Bem-vindo usuario")

if ativo is True:
    print("Você precisa ativar sua conta")
else:
    print("Ola como vai..")