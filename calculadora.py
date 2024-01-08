# Calculadora em Python

print("\n******************* Calculadora em Python *******************")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Não existe divisão por zero."

continuar = True

while continuar:
    print("\nSelecione o número da operação desejada: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Parar a calculadora")

    escolha = input("\nDigite sua opção (1/2/3/4/5): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))

        if escolha == '1':
            print("\n")
            print(num1, "+", num2, "=", soma(num1, num2))
            print("\n")

        elif escolha == '2':
            print("\n")
            print(num1, "-", num2, "=", subtracao(num1, num2))
            print("\n")

        elif escolha == '3':
            print("\n")
            print(num1, "*", num2, "=", multiplicacao(num1, num2))
            print("\n")

        elif escolha == '4':
            print("\n")
            print(num1, "/", num2, "=", divisao(num1, num2))
            print("\n")

    elif escolha == '5':
        continuar = False
        print("Calculadora encerrada.")

    else:
        print("\nOpção Inválida!")

print("Obrigado por usar a calculadora!")