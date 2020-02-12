#
#   Recebendo dados do usuário
#

#   Entrada de dados
#   print ("Qual é seu nome..?")
#   nome=input()

nome=input("qual seu nome..?")

#   Exemplo de PRINT antigo
#   print ("Seja bem-Vindo(a) %s" %(nome))

#   exemplo de PRINT moderno 3.X
#   print("Seja bem-vindo(a) {0}".format(nome))

#   Exemplo de PRINT atual 3.7
print(f"Seja bem-vindo(a) {nome}")

#   print("Qual sua Idade..?")
#   idade = input()

idade = input("Qual sua idade..?")
#   Processamento

#   Saída de dados
#   print("A %s tem %s anos" %(nome, idade))

#   Exemplo de PRINT moderno 3.X
#   print ("A {0} tem {1} anos".format(nome, idade))

#   Exemplo de PRINT atual 3.7
print(f"A {nome} tem {idade} anos")

#   int(idade)  ==> CAST
#   CAST é a conversão de um tipo da dado para outro
print(f"A {nome} nasceu em {2020 - int(idade)}")


