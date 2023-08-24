def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior(a, b):
    return max(a, b)

def menor(a, b):
    return min(a, b)

while True:
    print("Escolha uma operação:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior")
    print("d. Menor")
    print("e. Sair do programa")

    opcao = input("Digite a opção desejada: ")

    if opcao == 'e':
        break

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == 'a':
        print("Resultado:", somar(valor1, valor2))
    elif opcao == 'b':
        print("Resultado:", multiplicar(valor1, valor2))
    elif opcao == 'c':
        print("Maior valor:", maior(valor1, valor2))
    elif opcao == 'd':
        print("Menor valor:", menor(valor1, valor2))