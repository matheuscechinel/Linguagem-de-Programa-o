print("Escolha uma opção:")
print("a. Soma de 2 números.")
print("b. Diferença entre 2 números (maior pelo menor).")
print("c. Produto entre 2 números.")
print("d. Divisão entre 2 números (o denominador não pode ser zero).")

opcao = input("Digite a opção desejada: ")

if opcao in ['a', 'b', 'c', 'd']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 'a':
        resultado = num1 + num2
    elif opcao == 'b':
        resultado = abs(num1 - num2)
    elif opcao == 'c':
        resultado = num1 * num2
    elif opcao == 'd':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            exit()

    print("Resultado:", resultado)
else:
    print("Opção inválida.")