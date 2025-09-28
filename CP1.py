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



# 7. Login simples
# Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.

# usuario = input("Digite o nome do usuário: ")
# senha = input("Digite a senha: ")
# if usuario == "admin" and senha == "1234":
#     print("Acesso permitido")
# else:
#     print("Acesso negado")



# 8. Par ou múltiplo de 5
# Solicite um número inteiro e verifique:

# Se ele é par, escreva “Par”.

# Senão, se for múltiplo de 5, escreva “Múltiplo de 5”.

# Caso contrário, escreva “Outro número”.

# numero = int(input("Digite um numero inteiro: "))
# if numero % 2 == 0:
#     print("Par")
# elif numero % 5 == 0:
#     print("Múltiplo de 5")
# else: 
#     print("Outro número")



# 9. Conversão de temperatura
# Peça ao usuário uma temperatura em graus Celsius e mostre se está:

# Abaixo de 0 → “Congelante”

# Entre 0 e 30 → “Agradável”

# Acima de 30 → “Quente”

# temperatura = float(input("Digite a temperatura em graus Celsius: "))

# if temperatura < 0:
#     print("Congelante")
# elif 0<= temperatura <= 30:
#     print("Agradavel")
# else:
#     print("Quente")

# 10. Calculadora simples

# Receba dois números inteiros e uma operação (+, -, *, /) digitada pelo usuário. Use if-else para calcular e mostrar o resultado.
numero_primeiro = int(input("Digite o primeiro número inteiro: "))
numero_segundo = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite qual operação gostaria (+, -, *, /): ")

if operacao == "+":
    print(numero_primeiro + numero_segundo)
elif operacao == "-":
    print(numero_primeiro - numero_segundo)
elif operacao == "*":
    print(numero_primeiro * numero_segundo)
elif operacao == "/":
    print(numero_primeiro / numero_segundo)

else:
    print("invalido")