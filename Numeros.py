def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

while True:
    print("Selecione a operação.")
    print("1.Soma")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5.Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", soma(num1,num2))

    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1,num2))

    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1,num2))

    elif escolha == '4':
        print(num1, "/", num2, "=", divisao(num1,num2))
    else:
        print("Operação inválida")
        break