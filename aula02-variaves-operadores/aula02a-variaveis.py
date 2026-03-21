print("ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENAÇÃO DE STRINGS

#Comentários de 1 linha em python
'''
Comentários de
múltiplas
linhas
'''

# VARIÁVEIS
nome = "Matheus" # string - texto
idade = 18 # int - numero
peso = 62.0 # float - num. decimal

print(nome, idade, peso)
print(f"Oiii, {nome}!!!!")

#INPUTS - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Oiii", nome, "! Vc tem", idade, "anos")
print(f"Oiii {nome}! Vc tem {idade} anos")

nova_idade = idade + 1
print(nova_idade)
