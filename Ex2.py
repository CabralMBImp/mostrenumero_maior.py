# Pedimos o valor ao usuário e convertemos para número inteiro (int)
valor = int(input("Digite um número inteiro: "))

# Verificamos se é maior ou igual a zero
if valor >= 0:
    print("O valor é POSITIVO.")
else:
    # Se a condição acima for falsa (ou seja, menor que zero), cai aqui
    print("O valor é NEGATIVO.")