
# 5. Comparação de dois números
# Peça dois números inteiros e informe qual deles é maior ou se são iguais.

primeiro = int(input("Digite o primeiro número inteiro: "))
segundo = int(input("Digite o segundo número inteiro: "))

if primeiro > segundo:
    print("O primeiro número é maior")
elif segundo > primeiro:
    print("O segundo número é maior")
else:
    print("Os números são iguais")