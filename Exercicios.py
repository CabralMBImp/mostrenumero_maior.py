# Solicita os números e converte para inteiro
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verifica qual é o maior
if num1 > num2:
    print(f"O maior é: {num1}")
else:
    # Se num1 não é maior, ou num2 é o maior ou eles são iguais
    print(f"O maior é: {num2}")