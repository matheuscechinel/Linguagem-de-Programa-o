def main():
    numeros = []
    numero = int(input("Digite um número inteiro (ou 1000 para parar): "))

    while numero != 1000:
        numeros.append(numero)
        numero = int(input("Digite um número inteiro (ou 1000 para parar): "))

    quantidade_numeros = len(numeros)
    soma = sum(numeros)

    print("Quantidade de números digitados:", quantidade_numeros)
    print("Soma dos números digitados:", soma)


if _name_ == "_main_":
    main()