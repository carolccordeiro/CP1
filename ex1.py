#1. Número positivo ou negativo
#Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

numero = int(input("Digite um número inteiro: "))
if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("Zero")