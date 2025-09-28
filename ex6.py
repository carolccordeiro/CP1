
# 6. Desconto em produto
# Receba o valor de um produto e mostre o preço final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.

valor = float(input("Digite o valor do produto: R$ "))
if valor > 100:
    desconto = valor * 0.10
    preco_final = valor - desconto
    print("Seu preço com desconto é: ", preco_final)
else:
    print("Preço sem desconto é: ", valor)