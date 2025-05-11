# calculadora.py

print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha a operação (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == '2':
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == '3':
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == '4':
    if num2 == 0:
        print("Erro: divisão por zero!")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)
else:
    print("Operação inválida.")
