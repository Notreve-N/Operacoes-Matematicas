print("**Operações Matemáticas**")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Adição
soma = numero1 + numero2
print(f"Soma: {soma}")

# Subtração
subtracao = numero1 - numero2
print(f"Subtração: {subtracao}")

# Multiplicação
multiplicacao = numero1 * numero2
print(f"Multiplicação: {multiplicacao}")

# Divisão
if numero2 != 0:
    divisao = numero1 / numero2
    print(f"Divisão: {divisao}")
else:
    print("Divisão por zero não é permitida")

# Potência
potencia = numero1 ** numero2
print(f"Potência: {potencia}")