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