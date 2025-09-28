#1. Número positivo ou negativo
#Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

# numero = int(input("Digite um número inteiro: "))
# if numero > 0:
#     print("positivo")
# elif numero < 0:
#     print("negativo")
# else:
#     print("Zero")

#2. Par ou ímpar
#Receba um número inteiro e verifique se ele é par ou ímpar.

# numero = int(input("Digite um número inteiro: "))
# if numero % 2 == 0:
#     print("par")
# else:
#     print("impar")

# 3. Maioridade
# Solicite a idade de uma pessoa e mostre se ela é maior de idade (18 anos ou mais) ou menor de idade.

# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

# 4. Nota de aprovação
# Receba a nota de um aluno (0 a 10) e diga se ele foi aprovado (nota ≥ 6) ou reprovado.

# nota = int(input("Digite a nota do aluno (0 a 10): "))
# if nota >= 6:
#     print("Aprovado")

# else:
#     print("Reprovado")

# 5. Comparação de dois números
# Peça dois números inteiros e informe qual deles é maior ou se são iguais.

# primeiro = int(input("Digite o primeiro número inteiro: "))
# segundo = int(input("Digite o segundo número inteiro: "))

# if primeiro > segundo:
#     print("O primeiro número é maior")
# elif segundo > primeiro:
#     print("O segundo número é maior")
# else:
#     print("Os números são iguais")

# 6. Desconto em produto
# Receba o valor de um produto e mostre o preço final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.

# valor = float(input("Digite o valor do produto: R$ "))
# if valor > 100:
#     desconto = valor * 0.10
#     preco_final = valor - desconto
#     print("Seu preço com desconto é: ", preco_final)
# else:
#     print("Preço sem desconto é: ", valor)