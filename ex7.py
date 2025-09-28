# 7. Login simples
# Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")